// A text editor with unlimited undo/redo, and pluggable rendering.
//
//   Command    — every edit is an object that can execute() and undo() itself
//   Decorator  — renderers wrap renderers: Bold(UpperCase(Plain)) renders "**HELLO**"
#pragma once
#include <cstddef>
#include <memory>
#include <string>
#include <vector>

class Document {
public:
    const std::string& text() const { return text_; }
    // Both throw std::out_of_range if pos > size (or pos + len > size for erase).
    void insert(std::size_t pos, const std::string& s);
    std::string erase(std::size_t pos, std::size_t len);   // returns what was removed
private:
    std::string text_;
};

class Command {
public:
    virtual ~Command() = default;
    virtual void execute(Document& d) = 0;
    virtual void undo(Document& d) = 0;
};

class InsertCommand : public Command {
public:
    InsertCommand(std::size_t pos, std::string text);
    void execute(Document& d) override;
    void undo(Document& d) override;
private:
    std::size_t pos_;
    std::string text_;
};

class EraseCommand : public Command {
public:
    EraseCommand(std::size_t pos, std::size_t len);
    void execute(Document& d) override;
    void undo(Document& d) override;   // must restore exactly what execute() removed
private:
    std::size_t pos_, len_;
    std::string removed_;
};

class Editor {
public:
    // A command that throws on execute() must leave the document and both
    // stacks unchanged.
    void insert(std::size_t pos, const std::string& s);
    void erase(std::size_t pos, std::size_t len);
    bool undo();          // false when there is nothing to undo
    bool redo();          // false when there is nothing to redo; any new edit clears redo
    const std::string& text() const;
private:
    // Your members here.
};

// ---- rendering (decorator) ---------------------------------------------------
class Renderer {
public:
    virtual ~Renderer() = default;
    virtual std::string render(const std::string& text) const = 0;
};

class PlainRenderer : public Renderer {
public:
    std::string render(const std::string& text) const override;
};

// Base for decorators: owns the renderer it wraps.
class RendererDecorator : public Renderer {
public:
    explicit RendererDecorator(std::unique_ptr<Renderer> inner) : inner_(std::move(inner)) {}
protected:
    std::unique_ptr<Renderer> inner_;
};

class UpperCaseDecorator : public RendererDecorator {   // "hi" -> "HI"
public:
    using RendererDecorator::RendererDecorator;
    std::string render(const std::string& text) const override;
};

class BoldDecorator : public RendererDecorator {        // "hi" -> "**hi**"
public:
    using RendererDecorator::RendererDecorator;
    std::string render(const std::string& text) const override;
};

class LineNumberDecorator : public RendererDecorator {  // "a\nb" -> "1: a\n2: b"
public:
    using RendererDecorator::RendererDecorator;
    std::string render(const std::string& text) const override;
};
