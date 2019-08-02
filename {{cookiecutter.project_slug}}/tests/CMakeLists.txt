
# TEST EXECUTABLE
add_executable({{cookiecutter.library_name}}_tests
    {{cookiecutter.library_name}}.t.cpp
    tests.x.cpp
)

target_link_libraries({{cookiecutter.library_name}}_tests
	{{cookiecutter.library_name}}
	Catch2::Catch2
)

add_test(
    NAME {{cookiecutter.library_name}}_tests
    COMMAND {{cookiecutter.library_name}}_tests
)
