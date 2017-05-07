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


def readkey(getchar_fn=None, blocking=True):
    getchar = getchar_fn or readchar
    buffer = getchar(blocking)
    return buffer
