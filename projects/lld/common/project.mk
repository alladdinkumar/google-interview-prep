# Shared build rules. Each project's Makefile sets NAME and includes this.
#
#   make test     build and run the tests (the default)
#   make clean
#
# Needs a C++17 compiler with threads: g++ 9+ or clang 10+. On Windows, MSYS2's
# "mingw-w64-ucrt-x86_64-gcc" works; the old MinGW.org g++ 6.3 does not support
# std::thread.

CXX      ?= g++
CXXFLAGS ?= -std=c++17 -O1 -g -Wall -Wextra -pthread
SRC      := $(wildcard src/*.cpp)

test: build/tests
	./build/tests

build/tests: $(SRC) tests.cpp $(wildcard src/*.h) ../common/check.h
	@mkdir -p build
	$(CXX) $(CXXFLAGS) -Isrc -I../common $(SRC) tests.cpp -o build/tests

clean:
	rm -rf build

.PHONY: test clean
