import pytest
import sys


# ignore all tests in this folder if not on linux
def pytest_ignore_collect(path, config):
    if not sys.platform.startswith("linux"):
        return True

