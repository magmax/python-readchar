# -*- coding: utf-8 -*-
# Copyright (c) 2014 - 2017 Miguel Ángel García (@magmax9).
# Licensed under the MIT license.
# Inspired by:
# http://code.activestate.com/recipes/134892/#c9
# Thanks to Stephen Chappell (and  more recently,
#  guiweber - https://github.com/guiweber)


import msvcrt

from .key import windows_keys, windows_special_keys


def get_char(test_stream=None):
    """Get a linux character representation on Windows.  This
    representation will, for limited number of characters,
    be in the standard linux ^[[A type format and can
    be examined using the (for example) key.UP constant(s).
    """
    ch = msvcrt.getch()
    if ch in b'\x00\xe0':
        ch = msvcrt.getch()
        ch = repr(ch)[2:-1]
        ch = windows_special_keys.get(ch, ch)
    else:
        ch = repr(ch)[2:-1]
    if str(ch)[0] == '\\' or ch == ' ':
        ch = windows_keys.get(ch, ch)
    return test_stream or ch


def readchar(blocking=True):
    """gets a character or combo on windows and returns a string. If
    blocking is True then it will catch ctrl+c and not have them end
    the program. It will also wait for a key to be pressed before
    continuing on with the loop."""

    if blocking:
        return get_char()
    else:
        if msvcrt.kbhit():
            return get_char()
