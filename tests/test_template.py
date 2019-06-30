import json
import pathlib
from typing import Optional

import cookiecutter.main
import pytest


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


# Unit tests
def test_template(cookiecutter_renderer):
    cookiecutter_renderer()


@pytest.mark.parametrize('license', template_context()['license'])
def test_license_choices(license, cookiecutter_renderer):
    cookiecutter_renderer()
