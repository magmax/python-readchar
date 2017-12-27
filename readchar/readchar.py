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
    if not getchar_fn:
        # read first character from stdin
        c = readchar()
        ct = None
        # keep reading from stdin with NONBLOCK flag until it returns empty
        #  meaning stdin has no more characters stored
        while ct != '':
            ct = readchar(NONBLOCK=True)
            c += ct
        return c
    else:
        c1 = getchar_fn()
        if ord(c1) != 0x1b:
            return c1
        c2 = getchar_fn()
        if ord(c2) != 0x5b:
            return c1 + c2
        c3 = getchar_fn()
        if ord(c3) != 0x33:
            return c1 + c2 + c3
        c4 = getchar_fn()
        return c1 + c2 + c3 + c4
