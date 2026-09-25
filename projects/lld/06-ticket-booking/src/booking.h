// Movie ticket booking with seat holds that expire.
//
// A user first *holds* seats (all or nothing), then *confirms* the hold before it expires
// (payment happens in between). Many users race for the same seats from many threads;
// exactly one may win each seat.
//
// Time is passed in as seconds so tests are deterministic; nothing here reads a clock.
#pragma once
#include <cstdint>
#include <mutex>
#include <optional>
#include <string>
#include <vector>

struct Seat {
    int row, col;
    bool operator==(const Seat& o) const { return row == o.row && col == o.col; }
    bool operator<(const Seat& o) const { return row != o.row ? row < o.row : col < o.col; }
};

enum class HoldResult { Ok, SeatUnavailable, InvalidSeat, UnknownShow };

struct HoldOutcome {
    HoldResult result;
    std::int64_t holdId;   // valid when result == Ok
};

class BookingService {
public:
    // Holds last `holdSeconds`; a hold whose time has passed no longer blocks its seats.
    explicit BookingService(std::int64_t holdSeconds);

    void addShow(const std::string& showId, int rows, int cols);   // duplicate -> std::invalid_argument

    // All-or-nothing: either every seat is held for this user, or none is.
    HoldOutcome hold(const std::string& showId, const std::string& user,
                     const std::vector<Seat>& seats, std::int64_t now);

    // Turns a live hold into a booking. False if the hold is unknown, expired, released or
    // already confirmed.
    bool confirm(std::int64_t holdId, std::int64_t now);

    // Gives the seats back. False if the hold is not live.
    bool release(std::int64_t holdId, std::int64_t now);

    // Seats neither booked nor under a live hold, in (row, col) order.
    std::vector<Seat> available(const std::string& showId, std::int64_t now) const;

private:
    // Your members here.
};
