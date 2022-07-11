import pytest
import sys

# ignore all tests in this folder if not on windows
def pytest_ignore_collect(path, config):
    if sys.platform not in ("win32", "cygwin"):
        return True
