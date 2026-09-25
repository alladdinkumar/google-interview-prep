#include "booking.h"

#include <stdexcept>

#include "check.h"

BookingService::BookingService(std::int64_t holdSeconds) { (void)holdSeconds; NOT_IMPLEMENTED(); }

void BookingService::addShow(const std::string& showId, int rows, int cols) {
    (void)showId; (void)rows; (void)cols;
    NOT_IMPLEMENTED();
}

HoldOutcome BookingService::hold(const std::string& showId, const std::string& user,
                                 const std::vector<Seat>& seats, std::int64_t now) {
    (void)showId; (void)user; (void)seats; (void)now;
    NOT_IMPLEMENTED();
}

bool BookingService::confirm(std::int64_t holdId, std::int64_t now) { (void)holdId; (void)now; NOT_IMPLEMENTED(); }
bool BookingService::release(std::int64_t holdId, std::int64_t now) { (void)holdId; (void)now; NOT_IMPLEMENTED(); }

std::vector<Seat> BookingService::available(const std::string& showId, std::int64_t now) const {
    (void)showId; (void)now;
    NOT_IMPLEMENTED();
}
