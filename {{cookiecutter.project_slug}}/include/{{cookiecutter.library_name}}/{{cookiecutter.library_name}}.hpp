{%- if cookiecutter.documentation_generator != "None" -%}
/**
 **************************************************
 * @file     {{cookiecutter.library_name}}.hpp
 * @author   {{cookiecutter.full_name}}
 * @date     {% now 'local', '%Y-%m-%d' %}
 * @brief Some brief description about this module.
 * @details
 * Some long description about this module.
 *
 */

/** @mainpage {{cookiecutter.project_name}}
 *
 * This is a cool project that does such and such.
 *
 */

{% endif -%}
#pragma once

#include <string>

{% if cookiecutter.documentation_generator != "None" -%}
/*! @brief Some brief bla about {{cookiecutter.cpp_namespace}}.
 *  @details
 *  Some long bla about {{cookiecutter.cpp_namespace}}.
 */
{% endif -%}
namespace {{cookiecutter.cpp_namespace}} {
{% if cookiecutter.documentation_generator != "None" %}
/*! @brief Some brief bla about message().
 *  @details
 *  Some long bla about message().
 *
 *  @param recipient The thing or person that shall be greeted.
 *  @return message
 */
{%- endif %}
std::string message(const std::string &recipient);

} /* end namespace '{{cookiecutter.cpp_namespace}}' */
