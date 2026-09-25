#include <atomic>
#include <memory>
#include <set>
#include <string>
#include <thread>
#include <vector>

#include "check.h"
#include "parking_lot.h"

namespace {
using S = SpotSize;
ParkingLot lot(std::vector<std::vector<SpotSize>> floors) {
    return ParkingLot(std::move(floors), std::make_unique<NearestSmallestFirst>(), std::make_unique<HourlyPricing>());
}
}  // namespace

TEST(fitting_rules) {
    CHECK_EQ(fitting(VehicleType::Motorcycle).size(), 3u);
    CHECK(fitting(VehicleType::Motorcycle)[0] == S::Small);
    CHECK_EQ(fitting(VehicleType::Car).size(), 2u);
    CHECK(fitting(VehicleType::Truck) == std::vector<SpotSize>{S::Large});
}

TEST(pricing_first_fifteen_minutes_free_then_per_started_hour) {
    HourlyPricing p;
    CHECK_EQ(p.fee(VehicleType::Car, 15), 0);
    CHECK_EQ(p.fee(VehicleType::Car, 16), 5000);
    CHECK_EQ(p.fee(VehicleType::Car, 60), 5000);
    CHECK_EQ(p.fee(VehicleType::Car, 61), 10000);
    CHECK_EQ(p.fee(VehicleType::Truck, 125), 30000);
    CHECK_EQ(p.fee(VehicleType::Motorcycle, 30), 2000);
}

TEST(allocation_prefers_smallest_fitting_then_nearest) {
    auto l = lot({{S::Large, S::Medium, S::Small}, {S::Small}});
    auto m = l.park("M1", VehicleType::Motorcycle, 0);
    CHECK(m.has_value());
    CHECK(m->spot.size == S::Small);
    CHECK_EQ(m->spot.floor, 0);
    CHECK_EQ(m->spot.index, 2);
    auto c = l.park("C1", VehicleType::Car, 0);
    CHECK(c->spot.size == S::Medium);
}

TEST(full_lot_and_duplicate_plate_are_refused) {
    auto l = lot({{S::Large}});
    CHECK(l.park("T1", VehicleType::Truck, 0).has_value());
    CHECK(!l.park("T2", VehicleType::Truck, 0).has_value());
    auto l2 = lot({{S::Large, S::Large}});
    CHECK(l2.park("X", VehicleType::Car, 0).has_value());
    CHECK(!l2.park("X", VehicleType::Car, 1).has_value());
}

TEST(unpark_frees_the_spot_and_charges) {
    auto l = lot({{S::Medium}});
    auto t = l.park("C1", VehicleType::Car, 100);
    CHECK_EQ(l.freeSpots(S::Medium), 0u);
    CHECK_EQ(l.unpark(t->id, 190), 10000);
    CHECK_EQ(l.freeSpots(S::Medium), 1u);
    CHECK_EQ(l.parkedCount(), 0u);
}

TEST(bad_tickets_throw) {
    auto l = lot({{S::Medium}});
    auto t = l.park("C1", VehicleType::Car, 100);
    CHECK_THROWS(l.unpark(t->id + 999, 200));
    CHECK_THROWS(l.unpark(t->id, 50));
    l.unpark(t->id, 200);
    CHECK_THROWS(l.unpark(t->id, 300));    // already used
}

TEST(ticket_ids_are_unique_and_increasing) {
    auto l = lot({{S::Small, S::Small, S::Small}});
    auto a = l.park("A", VehicleType::Motorcycle, 0);
    auto b = l.park("B", VehicleType::Motorcycle, 0);
    CHECK(b->id > a->id);
}

TEST(concurrent_gates_never_double_allocate) {
    std::vector<SpotSize> floor(200, S::Medium);
    auto l = lot({floor, floor});            // 400 spots
    std::atomic<int> parked{0};
    std::vector<std::thread> gates;
    std::vector<std::vector<Spot>> got(8);
    for (int g = 0; g < 8; ++g) {
        gates.emplace_back([&, g] {
            for (int i = 0; i < 100; ++i) {  // 800 cars for 400 spots
                auto t = l.park("G" + std::to_string(g) + "-" + std::to_string(i), VehicleType::Car, 0);
                if (t) { ++parked; got[g].push_back(t->spot); }
            }
        });
    }
    for (auto& t : gates) t.join();
    CHECK_EQ(parked.load(), 400);
    CHECK_EQ(l.parkedCount(), 400u);
    CHECK_EQ(l.freeSpots(S::Medium), 0u);
    std::set<std::pair<int, int>> seen;
    for (auto& v : got) for (auto& s : v) seen.insert({s.floor, s.index});
    CHECK_EQ(seen.size(), 400u);
}

int main() { return run_all(); }
