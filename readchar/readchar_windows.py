# -*- coding: utf-8 -*-
# Copyright (c) 2014 - 2017 Miguel Ángel García (@magmax9).
# Licensed under the MIT license.
# Inspired by:
# http://code.activestate.com/recipes/134892/#c9
# Thanks to Stephen Chappell (and  more recently,
#  guiweber - https://github.com/guiweber)


import msvcrt


def readchar(blocking=False):
    """Get a single character on Windows."""

    while msvcrt.kbhit():
        msvcrt.getch()
    ch = msvcrt.getch()
    while ch.decode() in '\x00\xe0':
        msvcrt.getch()
        ch = msvcrt.getch()
    return ch.decode()
