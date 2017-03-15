# -*- coding: utf-8 -*-
# This file is based on this gist:
# http://code.activestate.com/recipes/134892/
# So real authors are DannyYoo and company.
import sys


if sys.platform.startswith('linux'):
    from .readchar_linux import readchar
elif sys.platform == 'darwin':
    from .readchar_linux import readchar
elif sys.platform in ('win32', 'cygwin'):
    from .readchar_windows import readchar
else:
    raise NotImplemented('The platform %s is not supported yet' % sys.platform)


def readkey(getchar_fn=None):
    getchar = getchar_fn or readchar
    c1 = getchar()
    if ord(c1) != 0x1b:
        return c1
    c2 = getchar()
    if ord(c2) != 0x5b:
        return c1 + c2
    c3 = getchar()
    if ord(c3) not in (0x31, 0x32, 0x33, 0x35, 0x36):
        return c1 + c2 + c3
    c4 = getchar()
    if ord(c4) not in (0x30, 0x31, 0x33, 0x34, 0x35, 0x36, 0x37, 0x38, 0x39):
        return c1 + c2 + c3 + c4
    c5 = getchar()
    return c1 + c2 + c3 + c4 + c5
