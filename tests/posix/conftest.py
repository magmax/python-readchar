import pytest
import sys

if sys.platform.startswith("linux"):
    import termios
    import tty
    import readchar.posix_read as linux_read


# ignore all tests in this folder if not on linux
def pytest_ignore_collect(path, config):
    if not sys.platform.startswith("linux"):
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
        return [None, None, None, 0, None, None, None]

    def mock_tcsetattr(fd, TCSADRAIN, old_settings):
        return None

    def mock_setraw(fd):
        return None

    def mock_kbhit():
        return True

    mock = mocked_stdin()
    with pytest.MonkeyPatch.context() as mp:
        mp.setattr(sys.stdin, "read", mock.read)
        mp.setattr(termios, "tcgetattr", mock_tcgetattr)
        mp.setattr(termios, "tcsetattr", mock_tcsetattr)
        mp.setattr(tty, "setraw", mock_setraw)
        mp.setattr(linux_read, "_kbhit", mock_kbhit)
        yield mock
