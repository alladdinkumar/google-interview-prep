#include "editor.h"

#include <stdexcept>

#include "check.h"

void Document::insert(std::size_t pos, const std::string& s) { (void)pos; (void)s; NOT_IMPLEMENTED(); }
std::string Document::erase(std::size_t pos, std::size_t len) { (void)pos; (void)len; NOT_IMPLEMENTED(); }

InsertCommand::InsertCommand(std::size_t pos, std::string text) : pos_(pos), text_(std::move(text)) {}
void InsertCommand::execute(Document& d) { (void)d; NOT_IMPLEMENTED(); }
void InsertCommand::undo(Document& d) { (void)d; NOT_IMPLEMENTED(); }

EraseCommand::EraseCommand(std::size_t pos, std::size_t len) : pos_(pos), len_(len) {}
void EraseCommand::execute(Document& d) { (void)d; NOT_IMPLEMENTED(); }
void EraseCommand::undo(Document& d) { (void)d; NOT_IMPLEMENTED(); }

void Editor::insert(std::size_t pos, const std::string& s) { (void)pos; (void)s; NOT_IMPLEMENTED(); }
void Editor::erase(std::size_t pos, std::size_t len) { (void)pos; (void)len; NOT_IMPLEMENTED(); }
bool Editor::undo() { NOT_IMPLEMENTED(); }
bool Editor::redo() { NOT_IMPLEMENTED(); }
const std::string& Editor::text() const { NOT_IMPLEMENTED(); }

std::string PlainRenderer::render(const std::string& text) const { (void)text; NOT_IMPLEMENTED(); }
std::string UpperCaseDecorator::render(const std::string& text) const { (void)text; NOT_IMPLEMENTED(); }
std::string BoldDecorator::render(const std::string& text) const { (void)text; NOT_IMPLEMENTED(); }
std::string LineNumberDecorator::render(const std::string& text) const { (void)text; NOT_IMPLEMENTED(); }
