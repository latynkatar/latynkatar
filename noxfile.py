"""Тэсты і іншая аўтаматызацыя для праекта."""

import glob
import os
import sys

import nox
import toml

nox.options.sessions = [
    "black_check",
    "isort_check",
    "ruff",
    "flake8",
    "pylint",
    "mypy",
    "pytest",
]


@nox.session
def black(session):
    """Фарматуе код па правілах black."""
    session.install("black")
    session.run("black", "tests", "src", "noxfile.py")


@nox.session(tags=["lint", "tests"])
def black_check(session):
    """паказвае што ў кодзе змяніў бы black."""
    session.install("black")
    session.run("black", "--check", "tests/", "src/", "noxfile.py")


@nox.session
def isort(session):
    """Выправўляе парадак імпартаў ў пітонаўскіх модулях"""
    session.install("isort")
    session.run("isort", "tests", "src", "noxfile.py")


@nox.session(tags=["lint", "tests"])
def isort_check(session):
    """Правярае парадак імпартаў ў пітонаўскіх модулях"""
    session.install("isort")
    session.run("isort", "--check-only", "tests", "src", "noxfile.py")


@nox.session(tags=["lint", "tests"])
def ruff(session):
    """Cтатычныя тэсты ruff."""
    session.install("ruff")
    session.run("ruff", "check", "tests/", "src/", "noxfile.py")


@nox.session(tags=["lint", "tests"])
def pylint(session):
    """Правярае код з дапамогай pylint."""
    session.install("pylint", "nox", "toml")
    session.run("pylint", "tests/", "src/", "noxfile.py")


@nox.session(tags=["lint", "tests"])
def flake8(session):
    """Правярае код з дапамогай flake8."""
    session.install("flake8", "flake8-pyproject")
    session.run("flake8", ".", "--count", "--exclude", ".nox,.venv")


@nox.session(tags=["lint", "tests"])
def mypy(session):
    """Правярае пазначэнне і супадзенне тыпаў праз mypy."""
    session.install("mypy")
    session.run("mypy", "-p", "src.latynkatar")


@nox.session(tags=["tests"])
def pytest(session):
    """Юніттэсты з pytest."""
    session.install("pytest", "pytest-html")
    if os.getenv("IS_THIS_A_PACKAGE_TEST") == "true":
        files = list(glob.glob("dist/*.whl"))
        if len(files) != 1:
            raise EnvironmentError(f"Found more then one WHL file in dist: {files}")
        session.install(files[0])
    session.run(
        "python3",
        "-m",
        "pytest",
        "tests",
        "-lvv",
        "-ra",
        "--log-cli-level=INFO",
        "--html=report.html",
        "--self-contained-html",
    )


@nox.session
def set_version(_):
    """Змяніць версію пакета."""
    with open("pyproject.toml", "r", encoding="utf-8") as config_file:
        config = toml.load(config_file)

    config["project"]["version"] = sys.argv[-1].split("/")[-1]

    with open("pyproject.toml", "w", encoding="utf-8") as config_file:
        toml.dump(config, config_file)


@nox.session
def generate_stubs(session):
    """Стварыць стабы для пакета Латынкатар"""
    session.install("mypy")
    session.run("stubgen", "--package", "src.latynkatar", "--output", ".")


@nox.session
def install_precommit(session):
    """Заінсталяаваць усе патрэбныя хукі"""
    session.run(
        "pre-commit",
        "install",
        "-t",
        "pre-commit",
        "-t",
        "pre-push",
        "-t",
        "post-checkout",
        external=True,
    )
