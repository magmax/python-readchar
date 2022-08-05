import pytest

from readchar import key as keys


defaultKeys = ["LF", "CR", "ENTER", "BACKSPACE", "SPACE", "ESC", "TAB"]
CTRLkeys = [
    "CTRL_A",
    "CTRL_B",
    "CTRL_C",
    "CTRL_D",
    "CTRL_E",
    "CTRL_F",
    "CTRL_G",
    "CTRL_H",
    "CTRL_I",
    "CTRL_J",
    "CTRL_K",
    "CTRL_L",
    "CTRL_M",
    "CTRL_N",
    "CTRL_O",
    "CTRL_P",
    "CTRL_Q",
    "CTRL_R",
    "CTRL_S",
    "CTRL_T",
    "CTRL_U",
    "CTRL_V",
    "CTRL_W",
    "CTRL_X",
    "CTRL_Y",
    "CTRL_Z",
]


@pytest.mark.parametrize("key", defaultKeys + CTRLkeys)
def test_defaultKeysExists(key):
    assert key in keys.__dict__


@pytest.mark.parametrize("key", defaultKeys + CTRLkeys)
def test_defaultKeysLength(key):
    assert 1 == len(keys.__dict__[key])


specialKeys = [
    "INSERT",
    "SUPR",
    "PAGE_UP",
    "PAGE_DOWN",
    "HOME",
    "END",
    "UP",
    "DOWN",
    "LEFT",
    "RIGHT",
    "F1",
    "F2",
    "F3",
    "F4",
    "F5",
    "F6",
    "F7",
    "F8",
    "F9",
    "F10",
    "F11",
    "F12",
]


@pytest.mark.parametrize("key", specialKeys)
def test_specialKeysExists(key):
    assert key in keys.__dict__


@pytest.mark.parametrize("key", specialKeys)
def test_specialKeysLength(key):
    assert 2 == len(keys.__dict__[key])
