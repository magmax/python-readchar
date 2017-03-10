# -*- coding: utf-8 -*-
# Initially taken from:
# http://code.activestate.com/recipes/134892/
# Thanks to Danny Yoo
import sys
import os
import select
import tty
import termios
from . import key


def readchar(wait_for_char=True):
    old_settings = termios.tcgetattr(sys.stdin)
    tty.setcbreak(sys.stdin.fileno())
    char_buffer = ''
    try:
        if wait_for_char or select.select([sys.stdin, ], [], [], 0.0)[0]:
            char = os.read(sys.stdin.fileno(), 1)
            char_buffer = char if type(char) is str else char.decode()
    except Exception:
        char_buffer = ''
    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)

    while True:
        if char_buffer not in key.ESCAPE_SEQUENCES:
            return char_buffer
        else:
            c = readchar(False)
            if c is None:
                return char_buffer
            else:
                char_buffer += c
