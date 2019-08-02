#include "{{cookiecutter.library_name}}/{{cookiecutter.library_name}}.hpp"

#include <catch2/catch.hpp>

namespace {{cookiecutter.cpp_namespace}} {
namespace testing {

TEST_CASE("message construction", "[message]" )
{
    REQUIRE(message(std::string{}) == "Hello");
    REQUIRE(message("World") == "Hello, World");
}

} /* end namespace 'testing' */
} /* end namespace '{{cookiecutter.cpp_namespace}}' */
