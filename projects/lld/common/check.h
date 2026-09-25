// Minimal test harness shared by every LLD project. No dependencies.
//
//   TEST(name) { CHECK(cond); CHECK_EQ(a, b); CHECK_THROWS(expr); }
//   int main() { return run_all(); }
//
// A test that throws (including the "not implemented" stubs) counts as a failure,
// so a fresh project compiles, runs, and reports 0/N instead of refusing to build.
#pragma once
#include <functional>
#include <iostream>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>

namespace check {
struct Case { std::string name; std::function<void()> fn; };
inline std::vector<Case>& registry() { static std::vector<Case> r; return r; }
struct Registrar { Registrar(const char* n, std::function<void()> f) { registry().push_back({n, std::move(f)}); } };
struct Failure : std::runtime_error { using std::runtime_error::runtime_error; };
}  // namespace check

#define CHECK_CAT2(a, b) a##b
#define CHECK_CAT(a, b) CHECK_CAT2(a, b)
#define TEST(name)                                                            \
    static void CHECK_CAT(test_, name)();                                     \
    static check::Registrar CHECK_CAT(reg_, name)(#name, CHECK_CAT(test_, name)); \
    static void CHECK_CAT(test_, name)()

#define CHECK(...)                                                                    \
    do { if (!(__VA_ARGS__)) { std::ostringstream os_; os_ << __FILE__ << ":" << __LINE__     \
         << "  CHECK(" #__VA_ARGS__ ") failed"; throw check::Failure(os_.str()); } } while (0)

#define CHECK_EQ(a, b)                                                                 \
    do { auto va_ = (a); auto vb_ = (b); if (!(va_ == vb_)) { std::ostringstream os_;   \
         os_ << __FILE__ << ":" << __LINE__ << "  CHECK_EQ(" #a ", " #b ") got "        \
             << va_ << " vs " << vb_; throw check::Failure(os_.str()); } } while (0)

#define CHECK_THROWS(...)                                                             \
    do {                                                                              \
        bool threw_ = false;                                                          \
        try { (void)(__VA_ARGS__); }                                                  \
        catch (const check::Failure&) { throw; }                                      \
        catch (const std::logic_error& e_) {                                          \
            if (std::string(e_.what()) == "not implemented") { throw; }               \
            threw_ = true;                                                            \
        }                                                                             \
        catch (...) { threw_ = true; }                                                \
        if (!threw_) {                                                                \
            std::ostringstream os_;                                                   \
            os_ << __FILE__ << ":" << __LINE__ << "  expected " #__VA_ARGS__ " to throw"; \
            throw check::Failure(os_.str());                                          \
        }                                                                             \
    } while (0)

inline int run_all() {
    int passed = 0;
    for (auto& c : check::registry()) {
        try {
            c.fn();
            ++passed;
            std::cout << "  PASS  " << c.name << "\n";
        } catch (const std::exception& e) {
            std::cout << "  FAIL  " << c.name << "  -- " << e.what() << "\n";
        } catch (...) {
            std::cout << "  FAIL  " << c.name << "  -- unknown exception\n";
        }
    }
    std::cout << "\n" << passed << "/" << check::registry().size() << " tests passed\n";
    return passed == static_cast<int>(check::registry().size()) ? 0 : 1;
}

// Every stub throws this. Replace the body; delete the throw.
#define NOT_IMPLEMENTED() throw std::logic_error("not implemented")
