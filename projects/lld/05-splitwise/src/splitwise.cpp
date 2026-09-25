#include "splitwise.h"

#include <stdexcept>

#include "check.h"

std::map<std::string, Paise> EqualSplit::split(Paise amount, const std::vector<std::string>& users) const {
    (void)amount; (void)users;
    NOT_IMPLEMENTED();
}

ExactSplit::ExactSplit(std::map<std::string, Paise> shares) : shares_(std::move(shares)) {}
std::map<std::string, Paise> ExactSplit::split(Paise amount, const std::vector<std::string>& users) const {
    (void)amount; (void)users;
    NOT_IMPLEMENTED();
}

PercentSplit::PercentSplit(std::map<std::string, int> percents) : percents_(std::move(percents)) {}
std::map<std::string, Paise> PercentSplit::split(Paise amount, const std::vector<std::string>& users) const {
    (void)amount; (void)users;
    NOT_IMPLEMENTED();
}

void ExpenseManager::addUser(const std::string& user) { (void)user; NOT_IMPLEMENTED(); }
void ExpenseManager::addExpense(const std::string& paidBy, Paise amount,
                                const std::vector<std::string>& participants, const SplitStrategy& how) {
    (void)paidBy; (void)amount; (void)participants; (void)how;
    NOT_IMPLEMENTED();
}
Paise ExpenseManager::balance(const std::string& user) const { (void)user; NOT_IMPLEMENTED(); }
std::vector<Payment> ExpenseManager::simplify() const { NOT_IMPLEMENTED(); }
