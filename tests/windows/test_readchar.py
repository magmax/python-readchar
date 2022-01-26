import pytest
from string import printable
from readchar import readchar, key


@pytest.mark.parametrize("c", printable)
def test_printableCharacters(patched_stdin, c):
    patched_stdin.push(c)
    assert c == readchar()


@pytest.mark.parametrize(
    ["seq", "key"],
    [
        ("\n", key.LF),
        ("\n", key.ENTER),
        ("\r", key.CR),
        ("\x08", key.BACKSPACE),
        ("\x20", key.SPACE),
        ("\x1b", key.ESC),
        ("\t", key.TAB),
    ],
)
def test_controlCharacters(seq, key, patched_stdin):
    patched_stdin.push(seq)
    assert key == readchar()
