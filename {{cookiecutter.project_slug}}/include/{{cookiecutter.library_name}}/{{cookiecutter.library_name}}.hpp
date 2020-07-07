{%- if cookiecutter.documentation_generator == "doxygen" -%}
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
#pragma once

#include <string>

namespace {{cookiecutter.cpp_namespace}}
{

    std::string message(const std::string& recipient);

} /* end namespace '{{cookiecutter.cpp_namespace}}' */
