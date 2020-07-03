# cpplib-tools Cookiecutter Template

This project is a [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/)
template for creating a C++ library project, with tooling.

The main features of the C++ project are:
* CMake build system
* Catch2 for C++ unit tests

## Creating a C++ library from the template

```
$ pip3 install cookiecutter
$ cookiecutter https://github.com/nmusolino/cookiecutter-cpplib-tools
```

You will be prompted to enter an author name, a project name, and other
template parameters.  The main parameters are listed in the table below.

| Template parameter        | Usage                                                                         |
|---------------------------|-------------------------------------------------------------------------------|
| full_name                 | Author name.  Used in copyright notices and README file.                      |
| email                     | Email of the author. Not used anywhere yet.                                   |
| project_name              | Name of project.  Used in documentation.                                      |
| project_slug              | Short name of project, used in filenames.  Should not include whitespace.     |
| library_name              | Used in C++ library name, which will be `lib<library_name>`.                  |
| cpp_namespace             | Namespace used in C++ files:  `namespace <cpp_namespace> { ... }`             |
| project_short_description | Description of project. Used in LICENSE                                       |
| version                   | Semantic versioning number of the project at creation. Not used anywhere yet. |
| license                   | License under which the project shall be published.                           |
| unit_test_framework       | Unit test framework that shall be used in the project.                        |
| use_boost                 | Choice whether boost library shall be used in the unit tests.                 |

## Building the C++ project

```
$ cd my_project
$ mkdir build
$ cd build
$ cmake ..
$ cmake --build .
$ ctest   # run C++ unit tests
```

## Contributing to the `cookiecutter-cpplib-tools` project

To contribute to this cookiecutter template project, check out the
repository and run the tests.

```
$ git clone https://github.com/nmusolino/cookiecutter-cpplib-tools
$ cd cookiecutter-cpplib-tools
$ pip3 install pipenv    
$ pipenv install --dev
$ pipenv run pytest    # Run tests of the template 
```

## License

This project is licensed under the GNU General Public License, version 3.  See the [LICENSE](LICENSE) file for details.


## Acknowledgements:

This cookiecutter incorporates ideas and code snippets from the following projects:
 - [cc-cpp-dll]https://github.com/numengo/cc-cpp-dll
 - [cookiecutter-pypackage]https://github.com/audreyr/cookiecutter-pypackage




