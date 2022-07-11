import msvcrt
import sys

import key


# Initially taken from:
# http://code.activestate.com/recipes/134892/#c9
# Thanks to Stephen Chappell
win_encoding = "mbcs"
XE0_OR_00 = "\x00\xe0"


def readchar():
    "Get a single character on Windows."

    while msvcrt.kbhit():
        msvcrt.getch()
    ch = msvcrt.getch()
    # print('ch={}, type(ch)={}'.format(ch, type(ch)))
    # while ch.decode(win_encoding) in unicode('\x00\xe0', win_encoding):
    while ch.decode(win_encoding) in XE0_OR_00:
        # print('found x00 or xe0')
        msvcrt.getch()
        ch = msvcrt.getch()

    return ch if sys.version_info.major > 2 else ch.decode(encoding=win_encoding)


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
