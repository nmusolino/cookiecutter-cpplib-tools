cmake_minimum_required(VERSION 3.14)

project({{cookiecutter.project_slug}}
    VERSION {{cookiecutter.version}} # bump this
    DESCRIPTION "{{cookiecutter.project_short_description}}"
)

set(CMAKE_CXX_STANDARD 17)


{%- if cookiecutter.unit_test_framework == "Catch2" %}
## EXTERNAL LIBRARIES
# Catch2 unit testing library.
add_subdirectory(external/Catch2)
{% endif %}

{%- if cookiecutter.use_sanitizers_cmake == "yes" %}
# Sanitizers-CMake package. Enable with '-DSANITIZE_UNDEFINED=On' at CMake command line.
set(CMAKE_MODULE_PATH
    "${CMAKE_SOURCE_DIR}/external/sanitizers-cmake/cmake" ${CMAKE_MODULE_PATH}
)
find_package(Sanitizers)
{%- endif %}

## LIBRARIES
# {{cookiecutter.library_name}} library
add_library({{cookiecutter.library_name}}
    include/{{cookiecutter.library_name}}/{{cookiecutter.library_name}}.hpp
    src/{{cookiecutter.library_name}}.cpp
)

target_include_directories({{cookiecutter.library_name}}
    PUBLIC include
)

{% if cookiecutter.unit_test_framework != "None" %}
## UNIT TEST SUITE
enable_testing()
add_subdirectory(tests)
{% endif %}

{% if cookiecutter.documentation_generator == "sphinx" -%}
set(CMAKE_MODULE_PATH "${PROJECT_SOURCE_DIR}/cmake" ${CMAKE_MODULE_PATH})
{% endif %}


{% if cookiecutter.documentation_generator != "None" -%}
add_subdirectory("docs")
{% endif %}
