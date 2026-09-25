#include "parking_lot.h"

#include <stdexcept>

#include "check.h"

std::vector<SpotSize> fitting(VehicleType v) { (void)v; NOT_IMPLEMENTED(); }

int NearestSmallestFirst::choose(const std::vector<Spot>& free, VehicleType v) const {
    (void)free; (void)v;
    NOT_IMPLEMENTED();
}

std::int64_t HourlyPricing::fee(VehicleType v, std::int64_t minutes) const {
    (void)v; (void)minutes;
    NOT_IMPLEMENTED();
}

ParkingLot::ParkingLot(std::vector<std::vector<SpotSize>> floors,
                       std::unique_ptr<AllocationStrategy> allocation,
                       std::unique_ptr<PricingStrategy> pricing) {
    (void)floors; (void)allocation; (void)pricing;
    NOT_IMPLEMENTED();
}

std::optional<Ticket> ParkingLot::park(const std::string& plate, VehicleType v, std::int64_t minute) {
    (void)plate; (void)v; (void)minute;
    NOT_IMPLEMENTED();
}

std::int64_t ParkingLot::unpark(std::int64_t ticketId, std::int64_t exitMinute) {
    (void)ticketId; (void)exitMinute;
    NOT_IMPLEMENTED();
}

std::size_t ParkingLot::freeSpots(SpotSize s) const { (void)s; NOT_IMPLEMENTED(); }
std::size_t ParkingLot::parkedCount() const { NOT_IMPLEMENTED(); }
