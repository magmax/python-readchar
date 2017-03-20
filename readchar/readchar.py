# -*- coding: utf-8 -*-
# Copyright (c) 2014- 2017 Miguel Ángel García (@magmax9).
# Based on previous work on gist getch()-like unbuffered character
# reading from stdin on both Windows and Unix (Python recipe),
# started by Danny Yoo. Licensed under the MIT license.

from __future__ import absolute_import
import sys


platform = sys.platform[0:5]
if platform in ("linux", "darwi"):
    from .readchar_linux import get_char, read_char
elif platform in ('win32', 'cygwin'):
    from .readchar_windows import get_char, read_char
else:
    raise NotImplemented('The platform %s is not supported yet' % sys.platform)


def readkey(test_stream=None):
    charbuffer = get_char(test_stream)
    return charbuffer


def readchar(blocking=True):
    return read_char(blocking)
