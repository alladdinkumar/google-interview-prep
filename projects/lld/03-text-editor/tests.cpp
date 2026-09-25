#include <memory>
#include <random>
#include <string>
#include <vector>

#include "check.h"
#include "editor.h"

TEST(insert_and_erase_edit_the_text) {
    Editor e;
    e.insert(0, "hello");
    e.insert(5, " world");
    e.erase(0, 6);
    CHECK_EQ(e.text(), std::string("world"));
}

TEST(undo_reverses_in_order) {
    Editor e;
    e.insert(0, "abc");
    e.insert(3, "def");
    e.erase(1, 3);                 // "aef"
    CHECK(e.undo());
    CHECK_EQ(e.text(), std::string("abcdef"));
    CHECK(e.undo());
    CHECK_EQ(e.text(), std::string("abc"));
    CHECK(e.undo());
    CHECK_EQ(e.text(), std::string(""));
    CHECK(!e.undo());
}

TEST(redo_replays_and_new_edit_clears_it) {
    Editor e;
    e.insert(0, "ab");
    e.insert(2, "cd");
    e.undo();
    CHECK(e.redo());
    CHECK_EQ(e.text(), std::string("abcd"));
    e.undo();
    e.insert(2, "X");              // clears redo
    CHECK(!e.redo());
    CHECK_EQ(e.text(), std::string("abX"));
}

TEST(out_of_range_edit_changes_nothing) {
    Editor e;
    e.insert(0, "abc");
    CHECK_THROWS(e.insert(10, "x"));
    CHECK_THROWS(e.erase(2, 5));
    CHECK_EQ(e.text(), std::string("abc"));
    CHECK(e.undo());               // undoes the valid insert, not a failed one
    CHECK_EQ(e.text(), std::string(""));
    CHECK(!e.undo());
}

TEST(erase_undo_restores_exact_text) {
    Editor e;
    e.insert(0, "the quick brown fox");
    e.erase(4, 6);
    CHECK_EQ(e.text(), std::string("the brown fox"));
    e.undo();
    CHECK_EQ(e.text(), std::string("the quick brown fox"));
}

TEST(random_edits_undo_back_to_empty) {
    Editor e;
    std::mt19937 rng(7);
    std::vector<std::string> history{""};
    for (int i = 0; i < 500; ++i) {
        const std::string& t = e.text();
        if (t.empty() || rng() % 3) {
            std::size_t pos = t.empty() ? 0 : rng() % (t.size() + 1);
            e.insert(pos, std::string(1 + rng() % 3, static_cast<char>('a' + rng() % 26)));
        } else {
            std::size_t pos = rng() % t.size();
            e.erase(pos, 1 + rng() % (t.size() - pos));
        }
        history.push_back(e.text());
    }
    for (int i = static_cast<int>(history.size()) - 2; i >= 0; --i) {
        CHECK(e.undo());
        CHECK_EQ(e.text(), history[i]);
    }
}

TEST(decorators_stack) {
    std::unique_ptr<Renderer> r = std::make_unique<BoldDecorator>(
        std::make_unique<UpperCaseDecorator>(std::make_unique<PlainRenderer>()));
    CHECK_EQ(r->render("hello"), std::string("**HELLO**"));
}

TEST(line_numbers) {
    LineNumberDecorator r(std::make_unique<PlainRenderer>());
    CHECK_EQ(r.render("a\nb\nc"), std::string("1: a\n2: b\n3: c"));
}

int main() { return run_all(); }
