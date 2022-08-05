import pytest

from readchar import key, readkey


@pytest.mark.parametrize("key", ["\x03", key.CTRL_C])
def test_KeyboardInterrupt(key, patched_stdin):
    patched_stdin.push(key)
    with pytest.raises(KeyboardInterrupt):
        readkey()


def test_singleCharacter(patched_stdin):
    patched_stdin.push("a")
    assert "a" == readkey()


@pytest.mark.parametrize(
    ["seq", "key"],
    [
        ("\x00\x48", key.UP),
        ("\x00\x50", key.DOWN),
        ("\x00\x4b", key.LEFT),
        ("\x00\x4d", key.RIGHT),
    ],
)
def test_cursorsKeys(seq, key, patched_stdin):
    patched_stdin.push(seq)
    assert key == readkey()


@pytest.mark.parametrize(
    ["seq", "key"],
    [
        ("\x00\x52", key.INSERT),
        ("\x00\x53", key.SUPR),
        ("\x00\x47", key.HOME),
        ("\x00\x4f", key.END),
        ("\x00\x49", key.PAGE_UP),
        ("\x00\x51", key.PAGE_DOWN),
    ],
)
def test_navigationKeys(seq, key, patched_stdin):
    patched_stdin.push(seq)
    assert key == readkey()


@pytest.mark.parametrize(
    ["seq", "key"],
    [
        ("\x00\x3b", key.F1),
        ("\x00\x3c", key.F2),
        ("\x00\x3d", key.F3),
        ("\x00\x3e", key.F4),
        ("\x00\x3f", key.F5),
        ("\x00\x40", key.F6),
        ("\x00\x41", key.F7),
        ("\x00\x42", key.F8),
        ("\x00\x43", key.F9),
        ("\x00\x44", key.F10),
        ("\x00\x85", key.F11),
        ("\x00\x86", key.F12),
    ],
)
def test_functionKeys(seq, key, patched_stdin):
    patched_stdin.push(seq)
    assert key == readkey()
