{% if cookiecutter.documentation_generator != "None" -%}
/**
 **************************************************
 * @file     {{cookiecutter.library_name}}.cpp
 * @author   {{cookiecutter.full_name}}
 * @date     {% now 'local', '%Y-%m-%d' %}
 * @brief Some brief description about this module.
 * @details
 * Some long description about this module.
 *
 */

{% endif -%}
#include <{{cookiecutter.library_name}}/{{cookiecutter.library_name}}.hpp>

namespace {{cookiecutter.cpp_namespace}} {

std::string message(const std::string& recipient)
{
    const std::string greeting { "Hello" };
    return recipient.empty() ? greeting : greeting + ", " + recipient;
}

} /* end namespace '{{cookiecutter.cpp_namespace}}' */
