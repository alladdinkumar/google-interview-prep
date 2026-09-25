#include "notification.h"

#include <stdexcept>
#include <thread>

#include "check.h"

// ---- Message::Builder -------------------------------------------------------
Message::Builder& Message::Builder::to(std::string userId) { (void)userId; NOT_IMPLEMENTED(); }
Message::Builder& Message::Builder::subject(std::string s) { (void)s; NOT_IMPLEMENTED(); }
Message::Builder& Message::Builder::body(std::string b) { (void)b; NOT_IMPLEMENTED(); }
Message::Builder& Message::Builder::priority(Priority p) { (void)p; NOT_IMPLEMENTED(); }
Message Message::Builder::build() const { NOT_IMPLEMENTED(); }

// ---- ChannelFactory ---------------------------------------------------------
std::unique_ptr<Channel> ChannelFactory::create(ChannelType type) { (void)type; NOT_IMPLEMENTED(); }

// ---- Retry policies ---------------------------------------------------------
FixedRetry::FixedRetry(int attempts, std::chrono::milliseconds delay) : attempts_(attempts), delay_(delay) {}
int FixedRetry::attempts() const { NOT_IMPLEMENTED(); }
std::chrono::milliseconds FixedRetry::delayBefore(int attempt) const { (void)attempt; NOT_IMPLEMENTED(); }

ExponentialBackoff::ExponentialBackoff(int attempts, std::chrono::milliseconds base, std::chrono::milliseconds cap)
    : attempts_(attempts), base_(base), cap_(cap) {}
int ExponentialBackoff::attempts() const { NOT_IMPLEMENTED(); }
std::chrono::milliseconds ExponentialBackoff::delayBefore(int attempt) const { (void)attempt; NOT_IMPLEMENTED(); }

// ---- NotificationService ----------------------------------------------------
NotificationService::NotificationService(std::unique_ptr<RetryPolicy> policy,
                                         std::function<void(std::chrono::milliseconds)> sleeper) {
    (void)policy; (void)sleeper;
    NOT_IMPLEMENTED();
}
void NotificationService::registerChannel(std::unique_ptr<Channel> channel) { (void)channel; NOT_IMPLEMENTED(); }
void NotificationService::setOptOut(const std::string& userId, ChannelType type, bool optedOut) {
    (void)userId; (void)type; (void)optedOut;
    NOT_IMPLEMENTED();
}
void NotificationService::addListener(DeliveryListener* listener) { (void)listener; NOT_IMPLEMENTED(); }
std::set<ChannelType> NotificationService::send(const Message& m, const std::vector<ChannelType>& channels) {
    (void)m; (void)channels;
    NOT_IMPLEMENTED();
}
