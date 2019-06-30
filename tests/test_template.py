import contextlib
import json
import os
import pathlib
import shutil
import subprocess
from typing import Optional

import cookiecutter.main
import pytest


def has_build_tools() -> bool:
    return all(shutil.which(program) is not None for program in ['cmake', 'make'])

def template_directory() -> pathlib.Path:
    """ Return the root directory containing cookiecutter.json. """
    return pathlib.Path(__file__).parent.parent


def template_context() -> dict:
    with open(template_directory() / "cookiecutter.json") as f:
        return json.load(f)


@pytest.fixture()
def cookiecutter_renderer(tmp_path: pathlib.Path):
    """ Return a function that can perform cookiecutter rendering. """
    output_dir = (tmp_path / "output")
    output_dir.mkdir()

    def render_template(extra_context: Optional[dict] = None) -> pathlib.Path:
        """ Return the result of running cookiecutter with the given context. """
        return pathlib.Path(
            cookiecutter.main.cookiecutter(template=template_directory().as_posix(),
                                           no_input=True,
                                           extra_context=extra_context,
                                           output_dir=output_dir)
        )
    return render_template


# @contextlib.contextmanager
# def chdir(directory: pathlib.Path):
#     prev_cwd = pathlib.Path.cwd()
#     os.chdir(directory)
#     try:
#         yield
#     finally:
#         os.chdir(prev_cwd)


# Unit tests
def test_template(cookiecutter_renderer):
    cookiecutter_renderer()


@pytest.mark.parametrize('license', template_context()['license'])
def test_license_choices(license, cookiecutter_renderer):
    cookiecutter_renderer()


@pytest.mark.skipif(not has_build_tools(), reason='Does not have cmake and make')
def test_build(cookiecutter_renderer):
    project_path = cookiecutter_renderer()
    build_dir = (project_path / "build")
    build_dir.mkdir()
    cmake_result = subprocess.run(['cmake', '..'], cwd=build_dir, check=True)
    build_result = subprocess.run(['cmake', '--build', '.'], cwd=build_dir, check=True)