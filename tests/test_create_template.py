"""
test_create_template
--------------------
"""


import os
import subprocess

import pytest


def run_tox(package):
    """Run the tox suite of the newly created package."""
    try:
        subprocess.check_call(
            ["tox", package, "-c", os.path.join(package, "tox.ini"), "-e", "py"]
        )
    except subprocess.CalledProcessError as e:
        pytest.fail("Subprocess fail", pytrace=True)


def test_run_cookiecutter_and_package_tests(cookies, capsys):
    """Create a new package via cookiecutter and run its tests."""
    result = cookies.bake(extra_context={"package_name": "based-repo-bar"})

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == "based-repo-bar"
    assert result.project.isdir()
    assert result.project.join("src").isdir()
    assert result.project.join("src", "based-repo_bar", "__init__.py").isfile()

    run_tox(str(result.project))


def test_run_cookiecutter_and_package_tests_with_caped_prefix(cookies, capsys):
    """make sure it's also ok to use caped prefix."""
    result = cookies.bake(extra_context={"package_name": "caped-based-repo"})

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == "caped-based-repo"
    assert result.project.isdir()
    assert result.project.join("src").isdir()
    assert result.project.join("src", "caped_based-repo", "__init__.py").isfile()


def test_run_cookiecutter_select_packages(cookies, capsys):
    """make sure it's also ok to use caped prefix."""
    result = cookies.bake(
        extra_context={
            "package_name": "anything",
        }
    )

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == "anything"
    assert result.project.isdir()
    assert result.project.join("src").isdir()
    assert result.project.join("src", "anything", "__init__.py").isfile()
    assert result.project.join("src", "anything", "_tests").isfile()

    assert not result.project.join(
        "src", "anything", "_tests"
    ).isfile()
    assert not result.project.join("src", "anything").isfile()
   
