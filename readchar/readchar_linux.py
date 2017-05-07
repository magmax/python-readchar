# -*- coding: utf-8 -*-
# Copyright (c) 2014, 2015 Miguel Ángel García (@magmax9).
# Based on previous work on gist getch()-like unbuffered character
# reading from stdin on both Windows and Unix (Python recipe),
# started by Danny Yoo. Licensed under the MIT license.

import sys
import tty
import termios
from . import key


def readchar(blocking):
    old_settings = termios.tcgetattr(sys.stdin)
    tty.setcbreak(sys.stdin.fileno())
    charbuffer = ''

    while True:
        if charbuffer in key.ESCAPE_SEQUENCES:
            char1 = getkey(False, old_settings)
        else:
            char1 = getkey(blocking, old_settings)
        if (charbuffer + char1) not in key.ESCAPE_SEQUENCES:
            # escape sequence complete or not an escape character..
            return convertchar(charbuffer + char1)

        # handle cases where the escape is finished, but looks incomplete -
        # such as a plain old 'ESC' (\x1b) that is not followed by other
        # codes:
        if (charbuffer + char1) == charbuffer:
            return convertchar(charbuffer)

        charbuffer += char1


def getkey(blocking, old_settings):
    charbuffer = ''
    try:
        if blocking or select.select([sys.stdin, ], [], [], 0.0)[0]:
            char = os.read(sys.stdin.fileno(), 1)
            charbuffer = char if type(char) is str else char.decode()
    except Exception:
        pass
    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
    return charbuffer


def convertchar(charbuffer):
    if charbuffer in key.linux_keys:
        return key.linux_keys[charbuffer]
    return charbuffer
