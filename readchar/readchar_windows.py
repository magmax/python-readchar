# -*- coding: utf-8 -*-
# Initially taken from:
# http://code.activestate.com/recipes/134892/#c9
# Thanks to Stephen Chappell
import msvcrt
from .key_windows import windows_keys, windows_special_keys


def get_char():
    """Get a single character on Windows."""
    ch = msvcrt.getch()
    if ch in b'\x00\xe0':
        ch = msvcrt.getch()
        ch = repr(ch)[2:-1]
        ch = windows_special_keys.get(ch, ch)
    else:
        ch = repr(ch)[2:-1]
    if str(ch)[0] == '\\' or ch == ' ':
        ch = windows_keys.get(ch, ch)
    return ch


def readchar(blocking=False):
    """gets a character or combo on windows and returns a string.
    If blocking is True then it will catch ctrl+c and not have them end the program.
    It will also wait for a key to be pressed before continuing on with the loop."""
    if blocking:
        return get_char()
    else:
        if msvcrt.kbhit():
            return get_char()
