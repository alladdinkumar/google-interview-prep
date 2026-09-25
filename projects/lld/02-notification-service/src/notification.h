// Notification service: send one message over several channels, with retries,
// per-user preferences, and delivery events.
//
// Patterns this is built to exercise:
//   Builder   — Message::Builder validates before a Message can exist
//   Factory   — ChannelFactory maps a ChannelType to a Channel
//   Strategy  — RetryPolicy decides how many attempts and the backoff between them
//   Observer  — DeliveryListener is told about every attempt's outcome
#pragma once
#include <chrono>
#include <functional>
#include <map>
#include <memory>
#include <set>
#include <string>
#include <vector>

enum class ChannelType { Email, Sms, Push };
enum class Priority { Low, Normal, High };

class Message {
public:
    class Builder {
    public:
        Builder& to(std::string userId);
        Builder& subject(std::string s);
        Builder& body(std::string b);
        Builder& priority(Priority p);
        // Throws std::invalid_argument if the recipient or the body is empty.
        Message build() const;
    private:
        std::string to_, subject_, body_;
        Priority priority_ = Priority::Normal;
    };

    const std::string& to() const { return to_; }
    const std::string& subject() const { return subject_; }
    const std::string& body() const { return body_; }
    Priority priority() const { return priority_; }

private:
    Message() = default;          // only the Builder makes Messages
    std::string to_, subject_, body_;
    Priority priority_ = Priority::Normal;
};

// A delivery channel. send() returns true on success. Implementations must be safe to
// call repeatedly (retries).
class Channel {
public:
    virtual ~Channel() = default;
    virtual ChannelType type() const = 0;
    virtual bool send(const Message& m) = 0;
};

// Creates the production channel for a type. Tests replace channels through
// NotificationService::registerChannel, so this only needs to return the right type.
class ChannelFactory {
public:
    static std::unique_ptr<Channel> create(ChannelType type);
};

// Strategy for retrying. attempts() includes the first try.
class RetryPolicy {
public:
    virtual ~RetryPolicy() = default;
    virtual int attempts() const = 0;
    // Delay before attempt number `attempt` (2 = first retry).
    virtual std::chrono::milliseconds delayBefore(int attempt) const = 0;
};

class FixedRetry : public RetryPolicy {
public:
    FixedRetry(int attempts, std::chrono::milliseconds delay);
    int attempts() const override;
    std::chrono::milliseconds delayBefore(int attempt) const override;
private:
    int attempts_;
    std::chrono::milliseconds delay_;
};

// base, 2*base, 4*base, ... capped at `cap`.
class ExponentialBackoff : public RetryPolicy {
public:
    ExponentialBackoff(int attempts, std::chrono::milliseconds base, std::chrono::milliseconds cap);
    int attempts() const override;
    std::chrono::milliseconds delayBefore(int attempt) const override;
private:
    int attempts_;
    std::chrono::milliseconds base_, cap_;
};

struct DeliveryEvent {
    std::string userId;
    ChannelType channel;
    int attempt;
    bool success;
};

class DeliveryListener {
public:
    virtual ~DeliveryListener() = default;
    virtual void onDelivery(const DeliveryEvent& e) = 0;
};

class NotificationService {
public:
    // `sleeper` is called with each backoff delay instead of really sleeping, so tests
    // run instantly. Default: std::this_thread::sleep_for.
    explicit NotificationService(std::unique_ptr<RetryPolicy> policy,
                                 std::function<void(std::chrono::milliseconds)> sleeper = {});

    // Replace (or add) the channel used for a type.
    void registerChannel(std::unique_ptr<Channel> channel);

    // A user can opt out of a channel type. High-priority messages ignore opt-outs.
    void setOptOut(const std::string& userId, ChannelType type, bool optedOut);

    void addListener(DeliveryListener* listener);   // not owned

    // Sends over each requested channel the user has not opted out of, retrying per the
    // policy. Returns the set of channels that finally succeeded. A channel type with no
    // registered channel counts as a failure (no attempt, no event).
    std::set<ChannelType> send(const Message& m, const std::vector<ChannelType>& channels);

private:
    // Your members here.
};
