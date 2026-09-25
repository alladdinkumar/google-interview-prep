// A multi-floor parking lot, safe to use from many gates (threads) at once.
//
//   Strategy — AllocationStrategy picks the spot; PricingStrategy computes the fee
//   Thread safety — park() and unpark() may be called concurrently; a spot is never
//                   given to two vehicles and the counts never drift.
#pragma once
#include <cstdint>
#include <memory>
#include <mutex>
#include <optional>
#include <string>
#include <vector>

enum class VehicleType { Motorcycle, Car, Truck };
enum class SpotSize { Small, Medium, Large };

// Which spot sizes fit which vehicle:
//   Motorcycle -> Small, Medium, Large   (smallest first)
//   Car        -> Medium, Large
//   Truck      -> Large
std::vector<SpotSize> fitting(VehicleType v);

struct Spot {
    int floor;
    int index;        // position on the floor; lower = nearer the entrance
    SpotSize size;
};

struct Ticket {
    std::int64_t id;  // unique, increasing
    std::string plate;
    VehicleType vehicle;
    Spot spot;
    std::int64_t entryMinute;
};

class AllocationStrategy {
public:
    virtual ~AllocationStrategy() = default;
    // Index into `free` of the spot to use, or -1. `free` holds only spots that fit.
    virtual int choose(const std::vector<Spot>& free, VehicleType v) const = 0;
};

// Smallest fitting size first; among equal sizes, lowest floor, then lowest index.
class NearestSmallestFirst : public AllocationStrategy {
public:
    int choose(const std::vector<Spot>& free, VehicleType v) const override;
};

class PricingStrategy {
public:
    virtual ~PricingStrategy() = default;
    // Fee in paise for a stay of `minutes`.
    virtual std::int64_t fee(VehicleType v, std::int64_t minutes) const = 0;
};

// Per started hour: Motorcycle 2000, Car 5000, Truck 10000 paise. First 15 minutes free.
// 0-15 min -> 0; 16-60 -> 1 hour; 61-120 -> 2 hours; ...
class HourlyPricing : public PricingStrategy {
public:
    std::int64_t fee(VehicleType v, std::int64_t minutes) const override;
};

class ParkingLot {
public:
    // floors[f] lists the size of each spot on floor f, in index order.
    ParkingLot(std::vector<std::vector<SpotSize>> floors,
               std::unique_ptr<AllocationStrategy> allocation,
               std::unique_ptr<PricingStrategy> pricing);

    // A ticket, or nullopt when full for this vehicle or the plate is already parked.
    std::optional<Ticket> park(const std::string& plate, VehicleType v, std::int64_t minute);

    // The fee; frees the spot. Throws std::invalid_argument for an unknown or used ticket,
    // or if exitMinute < entryMinute.
    std::int64_t unpark(std::int64_t ticketId, std::int64_t exitMinute);

    std::size_t freeSpots(SpotSize s) const;
    std::size_t parkedCount() const;

private:
    // Your members here. One mutex is fine for this week; say what you would do at 1,000 gates.
};
