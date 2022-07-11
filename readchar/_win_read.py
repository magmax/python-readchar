import msvcrt

import key


def readchar() -> str:
    """Reads a single character from the input stream.
    Blocks until a character is available."""

    # manual byte decoding because some bytes in windows are not utf-8 encodable.
    return chr(int.from_bytes(msvcrt.getch(), "big"))


# Windows uses scan codes for extended characters. This dictionary translates
# scan codes to the unicode sequences expected by readkey.
#
# for windows scan codes see:
#   https://msdn.microsoft.com/en-us/library/aa299374
#      or
#   http://www.quadibloc.com/comp/scan.htm
xlate_dict = {
    59: key.F1,
    60: key.F2,
    61: key.F3,
    62: key.F4,
    63: key.F5,
    64: key.F6,
    65: key.F7,
    66: key.F8,
    67: key.F9,
    68: key.F10,
    133: key.F11,
    134: key.F12,
    # don't have table entries for...
    # CTR_A, ..
    # ALT_A, ..
    # CTRL-F1, ..
    # CTRL_ALT_SUPR,
    # CTRL_ALT_A, .., etc.
    82: key.INSERT,
    83: key.SUPR,  # key.py uses SUPR, not DELETE
    73: key.PAGE_UP,
    81: key.PAGE_DOWN,
    71: key.HOME,
    79: key.END,
    72: key.UP,
    80: key.DOWN,
    75: key.LEFT,
    77: key.RIGHT,
}


def readkey(getchar_fn=None):
    # Get a single character on Windows. if an extended key is pressed, the
    # Windows scan code is translated into a the unicode sequences readchar
    # expects (see key.py).
    while True:
        if msvcrt.kbhit():
            ch = msvcrt.getch()
            a = ord(ch)
            if a == 0 or a == 224:
                b = ord(msvcrt.getch())
                try:
                    return xlate_dict[b]
                except KeyError:
                    return None
            elif a == 8:
                return key.BACKSPACE
            elif a == 13:
                return key.ENTER
            else:
                return ch.decode()
