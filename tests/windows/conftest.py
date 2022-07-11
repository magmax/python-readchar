import pytest
import sys


if sys.platform in ("win32", "cygwin"):
    import msvcrt


# ignore all tests in this folder if not on windows
def pytest_ignore_collect(path, config):
    if sys.platform not in ("win32", "cygwin"):
        return True


@pytest.fixture
def patched_stdin():
    class mocked_stdin:
        def push(self, string):
            for c in string:
                msvcrt.ungetch(ord(c).to_bytes(1, "big"))

    return mocked_stdin()
