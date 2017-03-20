# -*- coding: utf-8 -*-
# Copyright (c) 2014- 2017 Miguel Ángel García (@magmax9).
# Based on previous work on gist getch()-like unbuffered character
# reading from stdin on both Windows and Unix (Python recipe),
# started by Danny Yoo. Licensed under the MIT license.

from __future__ import absolute_import
import sys


if sys.platform.startswith('linux'):
    from .readchar_linux import readchar, get_char
elif sys.platform == 'darwin':
    from .readchar_linux import readchar, get_char
elif sys.platform in ('win32', 'cygwin'):
    from .readchar_windows import readchar, get_char
else:
    raise NotImplemented('The platform %s is not supported yet' % sys.platform)


def readkey(getchar_func=get_char):
    getchar = getchar_func or readchar
    charbuffer = getchar()
    return charbuffer
