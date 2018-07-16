# -*- coding: utf-8 -*-
# Initially taken from:
# http://code.activestate.com/recipes/134892/#c9
# Thanks to Stephen Chappell
import msvcrt
import sys


win_encoding = 'mbcs'


XE0_OR_00 = '\x00\xe0'


def readchar(blocking=False):
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

    return (
        ch
        if sys.version_info.major > 2
        else ch.decode(encoding=win_encoding)
    )
