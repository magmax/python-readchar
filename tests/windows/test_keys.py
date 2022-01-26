import pytest
from readchar import key as keys


defaultKeys = ["LF", "CR", "ENTER", "BACKSPACE", "SPACE", "ESC", "TAB"]


@pytest.mark.parametrize("key", defaultKeys)
def test_defaultKeysExists(key):
    assert key in keys.__dict__


@pytest.mark.parametrize("key", defaultKeys)
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
