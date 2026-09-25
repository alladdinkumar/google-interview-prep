#include <chrono>
#include <list>
#include <random>
#include <string>
#include <vector>

#include "check.h"
#include "lru_cache.h"

TEST(rejects_zero_capacity) {
    CHECK_THROWS(LRUCache<int, int>(0));
}

TEST(get_returns_what_was_put) {
    LRUCache<int, std::string> c(2);
    c.put(1, "one");
    CHECK(c.get(1).has_value());
    CHECK_EQ(*c.get(1), std::string("one"));
    CHECK(!c.get(2).has_value());
    CHECK_EQ(c.size(), 1u);
}

TEST(evicts_least_recently_used) {
    LRUCache<int, int> c(2);
    c.put(1, 10);
    c.put(2, 20);
    c.get(1);          // 2 is now least recent
    c.put(3, 30);      // evicts 2
    CHECK(c.contains(1));
    CHECK(!c.contains(2));
    CHECK(c.contains(3));
    CHECK_EQ(c.size(), 2u);
}

TEST(overwrite_refreshes_recency_and_value) {
    LRUCache<int, int> c(2);
    c.put(1, 10);
    c.put(2, 20);
    c.put(1, 11);      // 2 is now least recent
    c.put(3, 30);
    CHECK_EQ(*c.get(1), 11);
    CHECK(!c.contains(2));
}

TEST(contains_does_not_touch_recency) {
    LRUCache<int, int> c(2);
    c.put(1, 10);
    c.put(2, 20);
    CHECK(c.contains(1));   // must not refresh 1
    c.put(3, 30);           // evicts 1
    CHECK(!c.contains(1));
}

TEST(listener_sees_every_eviction_but_not_erase) {
    LRUCache<int, int> c(1);
    std::vector<int> evicted;
    c.onEvict([&](const int& k, const int& v) { evicted.push_back(k * 100 + v); });
    c.put(1, 1);
    c.put(2, 2);            // evicts (1,1)
    c.erase(2);             // not an eviction
    c.put(3, 3);
    c.put(4, 4);            // evicts (3,3)
    CHECK_EQ(evicted.size(), 2u);
    CHECK_EQ(evicted[0], 101);
    CHECK_EQ(evicted[1], 303);
}

TEST(matches_a_reference_model_on_random_operations) {
    const std::size_t cap = 7;
    LRUCache<int, int> c(cap);
    std::list<std::pair<int, int>> model;   // front = most recent
    auto find = [&](int k) {
        for (auto it = model.begin(); it != model.end(); ++it) if (it->first == k) return it;
        return model.end();
    };
    std::mt19937 rng(42);
    for (int i = 0; i < 20000; ++i) {
        int k = static_cast<int>(rng() % 15);
        if (rng() % 2) {
            int v = static_cast<int>(rng() % 1000);
            c.put(k, v);
            auto it = find(k);
            if (it != model.end()) model.erase(it);
            else if (model.size() == cap) model.pop_back();
            model.emplace_front(k, v);
        } else {
            auto got = c.get(k);
            auto it = find(k);
            if (it == model.end()) {
                CHECK(!got.has_value());
            } else {
                CHECK(got.has_value());
                CHECK_EQ(*got, it->second);
                model.splice(model.begin(), model, it);
            }
        }
        CHECK_EQ(c.size(), model.size());
    }
}

TEST(a_million_operations_run_in_linear_time) {
    LRUCache<int, int> c(100000);
    auto start = std::chrono::steady_clock::now();
    for (int i = 0; i < 1000000; ++i) {
        c.put(i % 150000, i);
        c.get((i * 7) % 150000);
    }
    auto ms = std::chrono::duration_cast<std::chrono::milliseconds>(
                  std::chrono::steady_clock::now() - start).count();
    CHECK(ms < 5000);   // an O(n) get would take minutes
}

int main() { return run_all(); }
