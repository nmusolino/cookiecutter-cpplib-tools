cmake_minimum_required(VERSION 3.14)

project({{cookiecutter.project_slug}}
	VERSION {{cookiecutter.version}}
	DESCRIPTION "{{cookiecutter.project_short_description}}"
)

set(CMAKE_CXX_STANDARD 17)


{%- if cookiecutter.unit_test_framework == "Catch2" -%}
## EXTERNAL LIBRARIES
# Catch2 unit testing library.
add_subdirectory(external/Catch2)
{% endif %}

# Sanitizers-CMake package. Enable with '-DSANITIZE_UNDEFINED=On' at CMake command line.
set(CMAKE_MODULE_PATH
    "${CMAKE_SOURCE_DIR}/external/sanitizers-cmake/cmake" ${CMAKE_MODULE_PATH}
)
find_package(Sanitizers)


## LIBRARIES
# {{cookiecutter.library_name}} library
add_library({{cookiecutter.library_name}}
    include/{{cookiecutter.library_name}}/{{cookiecutter.library_name}}.hpp
    src/{{cookiecutter.library_name}}.cpp
)

target_include_directories({{cookiecutter.library_name}}
    PUBLIC include
)
	       	
	       	
{%- if cookiecutter.unit_test_framework != "None" -%}
## UNIT TEST SUITE
enable_testing()
add_subdirectory(tests)
{% endif %}


add_subdirectory("docs")
