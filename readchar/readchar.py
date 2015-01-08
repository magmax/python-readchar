# -*- coding: utf-8 -*-
# This file is based on this gist:
# http://code.activestate.com/recipes/134892/
# So real authors are DannyYoo and company.
import sys
import key

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
    c1 = getchar(True)
    if c1 != key.ESC:
        return c1
    c2 = getchar()
    if c2 is None:
        return c1
    if ord(c2) != 0x5b:
        return c1 + c2
    c3 = getchar()
    if ord(c3) != 0x33:
        return c1 + c2 + c3
    c4 = getchar()
    return c1 + c2 + c3 + c4
