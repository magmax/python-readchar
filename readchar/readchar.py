# -*- coding: utf-8 -*-
# This file is based on this gist:
# http://code.activestate.com/recipes/134892/
# So real authors are DannyYoo and company.
import sys

if sys.platform.startswith("linux"):
    from .readchar_linux import readchar
elif sys.platform == "darwin":
    from .readchar_linux import readchar
elif sys.platform in ("win32", "cygwin"):
    import msvcrt

    from . import key
    from .readchar_windows import readchar
else:
    raise NotImplementedError("The platform %s is not supported yet" % sys.platform)


if sys.platform in ("win32", "cygwin"):  # noqa: C901
    #
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
        # CTRL_ALT_A, # Ctrl-Alt-A, etc.
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

else:

    def readkey(getchar_fn=None):
        getchar = getchar_fn or readchar
        c1 = getchar()
        if ord(c1) != 0x1B:
            return c1
        c2 = getchar()
        if ord(c2) != 0x5B:
            return c1 + c2
        c3 = getchar()
        if ord(c3) != 0x33:
            return c1 + c2 + c3
        c4 = getchar()
        return c1 + c2 + c3 + c4
