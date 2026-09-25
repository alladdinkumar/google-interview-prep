#include <atomic>
#include <string>
#include <thread>
#include <vector>

#include "booking.h"
#include "check.h"

TEST(hold_then_confirm_books_the_seats) {
    BookingService b(300);
    b.addShow("s1", 2, 3);
    auto h = b.hold("s1", "u1", {{0, 0}, {0, 1}}, 0);
    CHECK(h.result == HoldResult::Ok);
    CHECK_EQ(b.available("s1", 10).size(), 4u);
    CHECK(b.confirm(h.holdId, 10));
    CHECK_EQ(b.available("s1", 10000).size(), 4u);   // booked seats never come back
}

TEST(hold_is_all_or_nothing) {
    BookingService b(300);
    b.addShow("s1", 1, 3);
    CHECK(b.hold("s1", "u1", {{0, 1}}, 0).result == HoldResult::Ok);
    auto h = b.hold("s1", "u2", {{0, 0}, {0, 1}}, 1);
    CHECK(h.result == HoldResult::SeatUnavailable);
    CHECK_EQ(b.available("s1", 1).size(), 2u);        // (0,0) was not taken by the failed hold
}

TEST(invalid_seat_and_unknown_show) {
    BookingService b(300);
    b.addShow("s1", 2, 2);
    CHECK(b.hold("s1", "u", {{2, 0}}, 0).result == HoldResult::InvalidSeat);
    CHECK(b.hold("s1", "u", {{0, -1}}, 0).result == HoldResult::InvalidSeat);
    CHECK(b.hold("nope", "u", {{0, 0}}, 0).result == HoldResult::UnknownShow);
    CHECK_THROWS(b.addShow("s1", 1, 1));
}

TEST(expired_holds_free_their_seats_and_cannot_confirm) {
    BookingService b(300);
    b.addShow("s1", 1, 1);
    auto h = b.hold("s1", "u1", {{0, 0}}, 0);
    CHECK(b.hold("s1", "u2", {{0, 0}}, 299).result == HoldResult::SeatUnavailable);
    auto h2 = b.hold("s1", "u2", {{0, 0}}, 300);   // expired exactly at 300
    CHECK(h2.result == HoldResult::Ok);
    CHECK(!b.confirm(h.holdId, 301));
    CHECK(b.confirm(h2.holdId, 301));
}

TEST(release_returns_seats_once) {
    BookingService b(300);
    b.addShow("s1", 1, 2);
    auto h = b.hold("s1", "u1", {{0, 0}}, 0);
    CHECK(b.release(h.holdId, 5));
    CHECK(!b.release(h.holdId, 6));
    CHECK(!b.confirm(h.holdId, 7));
    CHECK_EQ(b.available("s1", 7).size(), 2u);
}

TEST(confirm_twice_fails) {
    BookingService b(300);
    b.addShow("s1", 1, 1);
    auto h = b.hold("s1", "u1", {{0, 0}}, 0);
    CHECK(b.confirm(h.holdId, 1));
    CHECK(!b.confirm(h.holdId, 2));
}

TEST(available_is_sorted) {
    BookingService b(300);
    b.addShow("s1", 2, 2);
    b.hold("s1", "u", {{0, 1}}, 0);
    auto a = b.available("s1", 0);
    CHECK_EQ(a.size(), 3u);
    CHECK(a[0] == (Seat{0, 0}));
    CHECK(a[1] == (Seat{1, 0}));
    CHECK(a[2] == (Seat{1, 1}));
}

TEST(racing_users_one_winner_per_seat) {
    BookingService b(300);
    b.addShow("s1", 10, 10);
    std::atomic<int> wins{0};
    std::vector<std::thread> users;
    for (int u = 0; u < 16; ++u) {
        users.emplace_back([&, u] {
            for (int r = 0; r < 10; ++r)
                for (int c = 0; c < 10; ++c) {
                    auto h = b.hold("s1", "u" + std::to_string(u), {{r, c}}, 0);
                    if (h.result == HoldResult::Ok && b.confirm(h.holdId, 1)) ++wins;
                }
        });
    }
    for (auto& t : users) t.join();
    CHECK_EQ(wins.load(), 100);
    CHECK(b.available("s1", 5000).empty());
}

int main() { return run_all(); }
