import pytest
from readchar import readkey, key


def test_KeyboardInterrupt(patched_stdin):
    patched_stdin.push("\x03")
    with pytest.raises(KeyboardInterrupt):
        readkey()


def test_singleCharacter(patched_stdin):
    patched_stdin.push("a")
    assert "a" == readkey()


@pytest.mark.parametrize(
    ["seq", "key"],
    [
        ("\x1b\x5b\x41", key.UP),
        ("\x1b\x5b\x42", key.DOWN),
        ("\x1b\x5b\x44", key.LEFT),
        ("\x1b\x5b\x43", key.RIGHT),
    ],
)
def test_arrowKeys(seq, key, patched_stdin):
    patched_stdin.push(seq)
    assert key == readkey()


@pytest.mark.parametrize(
    ["seq", "key"],
    [
        ("\x1b\x5b\x32\x7e", key.INSERT),
        ("\x1b\x5b\x33\x7e", key.SUPR),
        ("\x1b\x5b\x48", key.HOME),
        ("\x1b\x5b\x46", key.END),
        ("\x1b\x5b\x35\x7e", key.PAGE_UP),
        ("\x1b\x5b\x36\x7e", key.PAGE_DOWN),
    ],
)
def test_specialKeys(seq, key, patched_stdin):
    patched_stdin.push(seq)
    assert key == readkey()


@pytest.mark.parametrize(
    ["seq", "key"],
    [
        (key.F1, "\x1b\x4f\x50"),
        (key.F2, "\x1b\x4f\x51"),
        (key.F3, "\x1b\x4f\x52"),
        (key.F4, "\x1b\x4f\x53"),
        (key.F5, "\x1b\x5b\x31\x35\x7e"),
        (key.F6, "\x1b\x5b\x31\x37\x7e"),
        (key.F7, "\x1b\x5b\x31\x38\x7e"),
        (key.F8, "\x1b\x5b\x31\x39\x7e"),
        (key.F9, "\x1b\x5b\x32\x30\x7e"),
        (key.F10, "\x1b\x5b\x32\x31\x7e"),
        (key.F11, "\x1b\x5b\x32\x33\x7e"),
        (key.F12, "\x1b\x5b\x32\x34\x7e"),
    ],
)
def test_functionKeys(seq, key, patched_stdin):
    patched_stdin.push(seq)
    assert key == readkey()
