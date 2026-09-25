#include <chrono>
#include <memory>
#include <vector>

#include "check.h"
#include "notification.h"

using namespace std::chrono_literals;

namespace {
// A channel that fails its first `failures` sends, then succeeds; counts calls.
class FakeChannel : public Channel {
public:
    FakeChannel(ChannelType t, int failures, int* calls) : t_(t), failures_(failures), calls_(calls) {}
    ChannelType type() const override { return t_; }
    bool send(const Message&) override { ++*calls_; return (*calls_) > failures_; }
private:
    ChannelType t_;
    int failures_;
    int* calls_;
};

struct Recorder : DeliveryListener {
    std::vector<DeliveryEvent> events;
    void onDelivery(const DeliveryEvent& e) override { events.push_back(e); }
};

Message msg(Priority p = Priority::Normal) {
    return Message::Builder().to("u1").subject("hi").body("hello").priority(p).build();
}
NotificationService service(int attempts, std::vector<std::chrono::milliseconds>* slept = nullptr) {
    return NotificationService(std::make_unique<FixedRetry>(attempts, 10ms),
                               [slept](std::chrono::milliseconds d) { if (slept) slept->push_back(d); });
}
}  // namespace

TEST(builder_validates_recipient_and_body) {
    CHECK_THROWS(Message::Builder().body("x").build());
    CHECK_THROWS(Message::Builder().to("u").build());
    Message m = Message::Builder().to("u").body("b").build();
    CHECK_EQ(m.to(), std::string("u"));
    CHECK(m.priority() == Priority::Normal);
}

TEST(factory_returns_the_requested_type) {
    CHECK(ChannelFactory::create(ChannelType::Email)->type() == ChannelType::Email);
    CHECK(ChannelFactory::create(ChannelType::Sms)->type() == ChannelType::Sms);
    CHECK(ChannelFactory::create(ChannelType::Push)->type() == ChannelType::Push);
}

TEST(exponential_backoff_doubles_and_caps) {
    ExponentialBackoff p(5, 100ms, 300ms);
    CHECK_EQ(p.attempts(), 5);
    CHECK(p.delayBefore(2) == 100ms);
    CHECK(p.delayBefore(3) == 200ms);
    CHECK(p.delayBefore(4) == 300ms);
    CHECK(p.delayBefore(5) == 300ms);
}

TEST(retries_until_success_and_sleeps_between) {
    int calls = 0;
    std::vector<std::chrono::milliseconds> slept;
    auto s = service(3, &slept);
    s.registerChannel(std::make_unique<FakeChannel>(ChannelType::Email, 2, &calls));
    auto ok = s.send(msg(), {ChannelType::Email});
    CHECK_EQ(calls, 3);
    CHECK(ok.count(ChannelType::Email) == 1);
    CHECK_EQ(slept.size(), 2u);
}

TEST(gives_up_after_the_policy_attempts) {
    int calls = 0;
    auto s = service(2);
    s.registerChannel(std::make_unique<FakeChannel>(ChannelType::Sms, 5, &calls));
    auto ok = s.send(msg(), {ChannelType::Sms});
    CHECK_EQ(calls, 2);
    CHECK(ok.empty());
}

TEST(listener_sees_every_attempt) {
    int calls = 0;
    Recorder r;
    auto s = service(3);
    s.addListener(&r);
    s.registerChannel(std::make_unique<FakeChannel>(ChannelType::Push, 1, &calls));
    s.send(msg(), {ChannelType::Push});
    CHECK_EQ(r.events.size(), 2u);
    CHECK(!r.events[0].success);
    CHECK_EQ(r.events[1].attempt, 2);
    CHECK(r.events[1].success);
}

TEST(opt_out_is_respected_unless_high_priority) {
    int calls = 0;
    auto s = service(1);
    s.registerChannel(std::make_unique<FakeChannel>(ChannelType::Sms, 0, &calls));
    s.setOptOut("u1", ChannelType::Sms, true);
    CHECK(s.send(msg(), {ChannelType::Sms}).empty());
    CHECK_EQ(calls, 0);
    CHECK(s.send(msg(Priority::High), {ChannelType::Sms}).count(ChannelType::Sms) == 1);
    CHECK_EQ(calls, 1);
}

TEST(missing_channel_fails_without_an_event) {
    Recorder r;
    auto s = service(3);
    s.addListener(&r);
    CHECK(s.send(msg(), {ChannelType::Email}).empty());
    CHECK(r.events.empty());
}

int main() { return run_all(); }
