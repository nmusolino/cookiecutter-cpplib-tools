cmake_minimum_required(VERSION 3.14)

project({{cookiecutter.project_slug}}
	VERSION {{cookiecutter.version}}
	DESCRIPTION "{{cookiecutter.project_short_description}}")

set(CMAKE_CXX_STANDARD 17)


## LIBRARIES
# Register Catch2 unit testing library.
add_subdirectory(external/Catch2)

# {{cookiecutter.library_name}} library
add_library({{cookiecutter.library_name}}
	    include/{{cookiecutter.library_name}}/{{cookiecutter.library_name}}.hpp
	    src/{{cookiecutter.library_name}}.cpp)

target_include_directories({{cookiecutter.library_name}}
			   PUBLIC include)
	       	

## UNIT TEST SUITE
enable_testing()
add_subdirectory(tests)

