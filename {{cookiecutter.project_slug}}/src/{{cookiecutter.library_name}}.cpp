#include <{{cookiecutter.library_name}}/{{cookiecutter.library_name}}.hpp>

namespace {{cookiecutter.cpp_namespace}} {

    std::string message(const std::string& recipient)
    {
        const std::string greeting { "Hello" };
        return recipient.empty() ? greeting : greeting + ", " + recipient;
    }

} /* end namespace '{{cookiecutter.cpp_namespace}}' */
