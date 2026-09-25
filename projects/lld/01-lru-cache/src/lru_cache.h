// A fixed-capacity least-recently-used cache.
//
// Every operation must be O(1) average. The classic shape is a doubly linked list
// (recency order) plus a hash map from key to list node — std::list and
// std::unordered_map<K, std::list<...>::iterator> are fine to use.
//
// Template code lives in the header, so the implementation goes here too.
#pragma once
#include <cstddef>
#include <functional>
#include <list>
#include <optional>
#include <stdexcept>
#include <unordered_map>
#include <utility>

#include "check.h"   // NOT_IMPLEMENTED()

template <typename K, typename V>
class LRUCache {
public:
    using EvictionListener = std::function<void(const K&, const V&)>;

    // capacity == 0 is a programming error: throw std::invalid_argument.
    explicit LRUCache(std::size_t capacity) : capacity_(capacity) { NOT_IMPLEMENTED(); }

    // The value for key, and marks it most recently used. std::nullopt if absent.
    std::optional<V> get(const K& key) { (void)key; NOT_IMPLEMENTED(); }

    // Insert or overwrite. Overwriting counts as a use. When inserting a new key into a
    // full cache, evict the least recently used entry first and notify every listener.
    void put(const K& key, const V& value) { (void)key; (void)value; NOT_IMPLEMENTED(); }

    // Remove key if present; returns whether it was there. Not an eviction: no listener call.
    bool erase(const K& key) { (void)key; NOT_IMPLEMENTED(); }

    // Does NOT count as a use.
    bool contains(const K& key) const { (void)key; NOT_IMPLEMENTED(); }

    std::size_t size() const { NOT_IMPLEMENTED(); }
    std::size_t capacity() const { return capacity_; }

    // Observer: called with (key, value) of every evicted entry, in registration order.
    void onEvict(EvictionListener listener) { (void)listener; NOT_IMPLEMENTED(); }

private:
    std::size_t capacity_;
    // Your members here.
};
