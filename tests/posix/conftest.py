import pytest
import sys

unix_like = sys.platform.startswith("linux") or "bsd" in sys.platform

if unix_like:
    import termios


# ignore all tests in this folder if not on a Unix-like platform
def pytest_ignore_collect(path, config):
    if not unix_like:
        return True


@pytest.fixture
def patched_stdin():
    class mocked_stdin:
        buffer = []

        def push(self, string):
            for c in string:
                self.buffer.append(c)

        def read(self, n):
            string = ""
            for i in range(n):
                string += self.buffer.pop(0)
            return string

    def mock_tcgetattr(fd):
        return [0, 0, 0, 0, None, None, None]

    def mock_tcsetattr(fd, TCSADRAIN, old_settings):
        return None

    mock = mocked_stdin()
    with pytest.MonkeyPatch.context() as mp:
        mp.setattr(sys.stdin, "read", mock.read)
        mp.setattr(termios, "tcgetattr", mock_tcgetattr)
        mp.setattr(termios, "tcsetattr", mock_tcsetattr)
        yield mock
