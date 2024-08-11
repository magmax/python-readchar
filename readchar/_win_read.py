import msvcrt

from ._config import config


def readchar() -> str:
    """Reads a single utf8-character from the input stream.
    Blocks until a character is available."""
    # read the first character.
    ch = [msvcrt.getwch()]

    # if the first character indicates a surrogate pair, read the second character.
    if 0xD800 <= ord(ch[0]) <= 0xDFFF:
        ch.append(msvcrt.getwch())

    # combine the characters into a single utf-16 encoded string.
    # this prevents the character from being treated as a surrogate pair again.
    return "".join(ch).encode("utf-16", errors="surrogatepass").decode("utf-16")


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
