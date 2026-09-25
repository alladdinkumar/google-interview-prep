// Expense sharing. Money is an integer number of paise — never a double.
//
//   Strategy — how an amount is divided: equally, by exact amounts, by percentages
//   Algorithm — simplify(): the fewest payments that settle every balance
#pragma once
#include <cstdint>
#include <map>
#include <memory>
#include <string>
#include <vector>

using Paise = std::int64_t;

// Returns each participant's share; the shares must sum to `amount` exactly.
class SplitStrategy {
public:
    virtual ~SplitStrategy() = default;
    virtual std::map<std::string, Paise> split(Paise amount, const std::vector<std::string>& users) const = 0;
};

// Equal shares; the leftover paise go one each to the first users in the given order.
// 100 among [a, b, c] -> a 34, b 33, c 33.
class EqualSplit : public SplitStrategy {
public:
    std::map<std::string, Paise> split(Paise amount, const std::vector<std::string>& users) const override;
};

// Exact shares given up front. Throws std::invalid_argument if they do not sum to amount
// or if the user lists differ.
class ExactSplit : public SplitStrategy {
public:
    explicit ExactSplit(std::map<std::string, Paise> shares);
    std::map<std::string, Paise> split(Paise amount, const std::vector<std::string>& users) const override;
private:
    std::map<std::string, Paise> shares_;
};

// Percentages (integers) that must sum to 100, else std::invalid_argument. Each share is
// floor(amount * pct / 100); leftover paise go one each to users in the given order.
class PercentSplit : public SplitStrategy {
public:
    explicit PercentSplit(std::map<std::string, int> percents);
    std::map<std::string, Paise> split(Paise amount, const std::vector<std::string>& users) const override;
private:
    std::map<std::string, int> percents_;
};

struct Payment {
    std::string from, to;
    Paise amount;
};

class ExpenseManager {
public:
    void addUser(const std::string& user);   // duplicate -> std::invalid_argument

    // `paidBy` paid `amount` for `participants` (who may include paidBy). Unknown users or
    // amount <= 0 -> std::invalid_argument.
    void addExpense(const std::string& paidBy, Paise amount,
                    const std::vector<std::string>& participants, const SplitStrategy& how);

    // Net balance: positive = is owed money, negative = owes. Sum over users is always 0.
    Paise balance(const std::string& user) const;

    // A list of payments that settles every balance, with at most (users with a non-zero
    // balance - 1) payments. Applying them makes every balance zero.
    std::vector<Payment> simplify() const;

private:
    // Your members here.
};
