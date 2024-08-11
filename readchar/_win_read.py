import msvcrt

from ._config import config


def readchar() -> str:
    """Reads a single utf8-character from the input stream.
    Blocks until a character is available."""

    # read a single wide character from the input.
    return msvcrt.getwch()


def readkey() -> str:
    """Reads the next keypress. If an escaped key is pressed, the full
    sequence is read and returned as noted in `_win_key.py`."""

    ch = readchar()

    if ch in config.INTERRUPT_KEYS:
        raise KeyboardInterrupt

    # if it is a normal character:
    if ch not in "\x00\xe0":
        return ch

    # if it is a scpeal key, read second half:
    ch2 = readchar()

    return "\x00" + ch2
