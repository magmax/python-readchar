import pytest
import sys
import select


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

    def mock_select(a, b, c, d):
        return [(sys.stdin)]

    mock = mocked_stdin()
    with pytest.MonkeyPatch.context() as mp:
        mp.setattr(sys.stdin, "read", mock.read)
        mp.setattr(select, "select", mock_select)
        yield mock
