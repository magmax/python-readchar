import sys

import pytest


# if sys.platform in ("win32", "cygwin"):
#     import msvcrt


# ignore all tests in this folder if not on windows
def pytest_ignore_collect(path, config):
    if sys.platform not in ("win32", "cygwin"):
        return True


@pytest.fixture
def patched_stdin(monkeypatch):
    class mocked_stdin:
        def push(self, string):
            # Create an iterator from the string
            characters = iter(string)

            # Patch msvcrt.getwch to return the next character from the iterator.
            monkeypatch.setattr("msvcrt.getwch", lambda: next(characters))

    return mocked_stdin()
