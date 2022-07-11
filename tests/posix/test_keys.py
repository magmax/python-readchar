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


len3_keys = ["UP", "DOWN", "LEFT", "RIGHT", "HOME", "END", "F1", "F2", "F3", "F4"]


@pytest.mark.parametrize("key", len3_keys)
def test_character_length_3_exists(key):
    assert key in keys.__dict__


@pytest.mark.parametrize("key", len3_keys)
def test_character_length_3_lenght(key):
    assert 3 == len(keys.__dict__[key])


len4_keys = ["INSERT", "SUPR", "PAGE_UP", "PAGE_DOWN"]


@pytest.mark.parametrize("key", len4_keys)
def test_character_length_4_exists(key):
    assert key in keys.__dict__


@pytest.mark.parametrize("key", len4_keys)
def test_character_length_4_lenght(key):
    assert 4 == len(keys.__dict__[key])


len5_keys = ["F5", "F6", "F7", "F8", "F9", "F10", "F11", "F12"]


@pytest.mark.parametrize("key", len5_keys)
def test_character_length_5_exists(key):
    assert key in keys.__dict__


@pytest.mark.parametrize("key", len5_keys)
def test_character_length_5_lenght(key):
    assert 5 == len(keys.__dict__[key])
