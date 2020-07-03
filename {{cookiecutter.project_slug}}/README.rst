{{cookiecutter.library_name}}
===============================================


Overview
========

{{ cookiecutter.project_short_description }}


Getting Started
---------------

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
See deployment for notes on how to deploy the project on a live system.

Prerequisites
~~~~~~~~~~~~~

What things you need to install the software and how to install them.

::

    Give examples


Building the C++ project
~~~~~~~~~~~~~~~~~~~~~~~~

```
$ cmake -S . -B build
$ cmake --build build
```


Installing
~~~~~~~~~~

A step by step series of examples that tell you how to get a development env running.

Say what the step will be

::

    Give the example

And repeat

::

    until finished

End with an example of getting some data out of the system or using it for a little demo

{%- if cookiecutter.unit_test_framework != "None" -%}
Running the tests
-----------------

```
$ cd build
$ ctest
```

Break down into end to end tests
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Explain what these tests test and why

::

    Give an example

And coding style tests
~~~~~~~~~~~~~~~~~~~~~~

Explain what these tests test and why

::

    Give an example
{% endif %}
    
Deployment
----------

Add additional notes about how to deploy this on a live system


Contributing
------------

Please read [CONTRIBUTING.rst] for details on our code of conduct, and the process for submitting pull requests to us.


Versioning
----------

We use `SemVer <http://semver.org/>`__ for versioning.


Authors
-------

See the list of `AUTHORS <AUTHORS.rst>`__ who helped creating {{cookiecutter.library_name}}.


License
-------

This project is licensed under the {{cookiecutter.license}} - see the `LICENSE <LICENSE>`__ file for details


Credits
-------

This package was created with `Cookiecutter <https://github.com/audreyr/cookiecutter>`__ and the `nmusolino/cookiecutter-cpplib-tools <https://github.com/nmusolino/cookiecutter-cpplib-tools>`__ project template.
