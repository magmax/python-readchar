# -*- coding: utf-8 -*-
# Initially taken from:
# http://code.activestate.com/recipes/134892/#c9
# Thanks to Stephen Chappell
import msvcrt


def readchar(blocking=False):
    "Get a single character on Windows."

    ch = msvcrt.getch()
    if ch in '\000\xe0':
        ch = msvcrt.getch()
    return repr(ch)[1:-1]
