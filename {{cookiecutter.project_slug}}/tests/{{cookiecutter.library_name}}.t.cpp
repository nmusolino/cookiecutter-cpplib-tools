#include "{{cookiecutter.library_name}}/{{cookiecutter.library_name}}.hpp"

#include <gtest/gtest.h>


namespace {{cookiecutter.cpp_namespace}} {
namespace testing {

    TEST(MessageTest, EmptyString)
    {
        EXPECT_EQ(message(std::string{}), "Hello");
    }

    TEST(MessageTest, NonemptyString)
    {
        EXPECT_EQ(message("World"), "Hello, World");
    }

} /* end namespace 'testing' */
} /* end namespace '{{cookiecutter.cpp_namespace}}' */
