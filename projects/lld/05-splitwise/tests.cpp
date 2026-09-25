#include <map>
#include <random>
#include <string>
#include <vector>

#include "check.h"
#include "splitwise.h"

namespace {
ExpenseManager group(const std::vector<std::string>& users) {
    ExpenseManager m;
    for (auto& u : users) m.addUser(u);
    return m;
}
}  // namespace

TEST(equal_split_distributes_leftover_paise) {
    auto s = EqualSplit().split(100, {"a", "b", "c"});
    CHECK_EQ(s["a"], 34);
    CHECK_EQ(s["b"], 33);
    CHECK_EQ(s["c"], 33);
}

TEST(exact_split_must_add_up) {
    CHECK_THROWS(ExactSplit({{"a", 50}, {"b", 40}}).split(100, {"a", "b"}));
    auto s = ExactSplit({{"a", 70}, {"b", 30}}).split(100, {"a", "b"});
    CHECK_EQ(s["a"], 70);
}

TEST(percent_split_validates_and_rounds) {
    CHECK_THROWS(PercentSplit({{"a", 50}, {"b", 40}}).split(100, {"a", "b"}));
    auto s = PercentSplit({{"a", 33}, {"b", 33}, {"c", 34}}).split(1001, {"a", "b", "c"});
    CHECK_EQ(s["a"] + s["b"] + s["c"], 1001);
    CHECK_EQ(s["c"], 340);
}

TEST(balances_track_who_owes_whom) {
    auto m = group({"a", "b", "c"});
    m.addExpense("a", 300, {"a", "b", "c"}, EqualSplit());
    CHECK_EQ(m.balance("a"), 200);
    CHECK_EQ(m.balance("b"), -100);
    CHECK_EQ(m.balance("c"), -100);
}

TEST(invalid_expenses_are_rejected) {
    auto m = group({"a", "b"});
    CHECK_THROWS(m.addUser("a"));
    CHECK_THROWS(m.addExpense("z", 100, {"a"}, EqualSplit()));
    CHECK_THROWS(m.addExpense("a", 0, {"a", "b"}, EqualSplit()));
    CHECK_THROWS(m.addExpense("a", 100, {"a", "zz"}, EqualSplit()));
    CHECK_EQ(m.balance("a"), 0);
}

TEST(simplify_settles_a_chain_in_one_payment) {
    auto m = group({"a", "b", "c"});
    m.addExpense("a", 100, {"b"}, EqualSplit());   // b owes a 100
    m.addExpense("b", 100, {"c"}, EqualSplit());   // c owes b 100
    auto p = m.simplify();
    CHECK_EQ(p.size(), 1u);
    CHECK_EQ(p[0].from, std::string("c"));
    CHECK_EQ(p[0].to, std::string("a"));
    CHECK_EQ(p[0].amount, 100);
}

TEST(simplify_zeroes_every_balance_within_the_bound) {
    std::vector<std::string> users;
    for (int i = 0; i < 10; ++i) users.push_back("u" + std::to_string(i));
    auto m = group(users);
    std::mt19937 rng(3);
    for (int e = 0; e < 60; ++e) {
        std::vector<std::string> who;
        for (auto& u : users) if (rng() % 2) who.push_back(u);
        if (who.empty()) who.push_back(users[0]);
        m.addExpense(users[rng() % users.size()], 1 + rng() % 10000, who, EqualSplit());
    }
    std::map<std::string, Paise> bal;
    std::size_t nonzero = 0;
    Paise total = 0;
    for (auto& u : users) { bal[u] = m.balance(u); total += bal[u]; if (bal[u]) ++nonzero; }
    CHECK_EQ(total, 0);
    auto pays = m.simplify();
    CHECK(pays.size() + 1 <= nonzero || nonzero == 0);
    for (auto& p : pays) { CHECK(p.amount > 0); bal[p.from] += p.amount; bal[p.to] -= p.amount; }
    for (auto& u : users) CHECK_EQ(bal[u], 0);
}

TEST(settled_group_needs_no_payments) {
    auto m = group({"a", "b"});
    m.addExpense("a", 100, {"b"}, EqualSplit());
    m.addExpense("b", 100, {"a"}, EqualSplit());
    CHECK(m.simplify().empty());
}

int main() { return run_all(); }
