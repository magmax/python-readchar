# -*- coding: utf-8 -*-
# Copyright (c) 2014 - 2017 Miguel Ángel García (@magmax9).
# Licensed under the MIT license.
# This code based on code snippet from the python 2 docs:
# https://docs.python.org/2/faq/library.html
#     #how-do-i-get-a-single-keypress-at-a-time


import sys
import os
import termios
import fcntl
from . import key


def get_char():
    charbuffer = b''
    while True:
        if charbuffer in key.ESCAPE_SEQUENCES:
            char1 = readchar(False)
        else:
            char1 = readchar()

        # return if escape sequence is finished (or not an escape sequence).
        if (charbuffer + char1) not in key.ESCAPE_SEQUENCES:
            # escape sequence complete or not an escape character..
            return charbuffer + char1

        # handle cases where the escape is finished, but looks incomplete -
        # such as a plain old 'ESC' (\x1b) that is not followed by other
        # codes:
        if (charbuffer + char1) == charbuffer:
            return charbuffer

        # add character to sequence and continue loop...
        charbuffer += char1


def readchar(blocking=True):
    fd = sys.stdin.fileno()
    oldterm = termios.tcgetattr(fd)

    newattr = termios.tcgetattr(fd)
    newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
    termios.tcsetattr(fd, termios.TCSANOW, newattr)

    oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
    fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)
    c = b''
    try:
        while blocking and c == b'':
            try:
                c = sys.stdin.read(1)
                break
            except IOError:
                pass
        else:
            if not blocking:
                try:
                    c = sys.stdin.read(1)
                except IOError:
                    pass
    finally:
        termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
        fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)
    return c
