# -*- coding: utf-8 -*-

import os
import sys
from io import open

from setuptools import find_packages, setup
from setuptools.command.test import test as TestCommand

version = "2.0.1"
github_ref = os.getenv("GITHUB_REF")
if github_ref and github_ref.startswith("refs/tags"):
    version = github_ref[10:]


def read_description():
    try:
        with open("README.rst", encoding="utf8") as fd:
            return fd.read()
    except:  # noqa
        return "Error found retrieving description"


class PyTest(TestCommand):
    user_options = [("pytest-args=", "a", "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = ["--cov-report=term-missing"]

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest

        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


setup(
    name="readchar",
    version=version,
    description="Utilities to read single characters and key-strokes",
    long_description=read_description(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development",
        "Topic :: Software Development :: User Interfaces",
    ],
    keywords="stdin,command line",
    author="Miguel Ángel García",
    author_email="miguelangel.garcia@gmail.com",
    url="https://github.com/magmax/python-readchar",
    license="MIT",
    packages=find_packages(exclude=["tests", "venv"]),
    include_package_data=True,
    zip_safe=False,
    cmdclass={"test": PyTest},
    tests_require=[
        "pexpect",
        "coverage",
        "pytest",
        "pytest-cov",
        "wheel",
    ],
    install_requires=[],
    setup_requires=[
        "flake8",
    ],
)
