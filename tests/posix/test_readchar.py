import pytest
from string import printable
from readchar import readchar, key


@pytest.mark.parametrize("c", printable)
def test_printableCharacters(patched_stdin, c):
    patched_stdin.push(c)
    assert c == readchar(blocking=True)


@pytest.mark.parametrize(
    ["seq", "key"],
    [
        ("\x0a", key.LF),
        ("\x0a", key.ENTER),
        ("\x0d", key.CR),
        ("\x7f", key.BACKSPACE),
        ("\x20", key.SPACE),
        ("\x1b", key.ESC),
        ("\x09", key.TAB),
    ],
)
def test_controlCharacters(seq, key, patched_stdin):
    patched_stdin.push(seq)
    assert key == readchar()


@pytest.mark.parametrize(
    ["seq", "key"],
    [
        ("\x01", key.CTRL_A),
        ("\x02", key.CTRL_B),
        ("\x03", key.CTRL_C),
        ("\x04", key.CTRL_D),
        ("\x05", key.CTRL_E),
        ("\x06", key.CTRL_F),
        ("\x07", key.CTRL_G),
        ("\x08", key.CTRL_H),
        ("\x09", key.CTRL_I),
        ("\x0a", key.CTRL_J),
        ("\x0b", key.CTRL_K),
        ("\x0c", key.CTRL_L),
        ("\x0d", key.CTRL_M),
        ("\x0e", key.CTRL_N),
        ("\x0f", key.CTRL_O),
        ("\x10", key.CTRL_P),
        ("\x11", key.CTRL_Q),
        ("\x12", key.CTRL_R),
        ("\x13", key.CTRL_S),
        ("\x14", key.CTRL_T),
        ("\x15", key.CTRL_U),
        ("\x16", key.CTRL_V),
        ("\x17", key.CTRL_W),
        ("\x18", key.CTRL_X),
        ("\x19", key.CTRL_Y),
        ("\x1a", key.CTRL_Z),
    ],
)
def test_CTRL_Characters(seq, key, patched_stdin):
    patched_stdin.push(seq)
    assert key == readchar()
