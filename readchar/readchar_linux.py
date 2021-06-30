# -*- coding: utf-8 -*-
# Initially taken from:
# http://code.activestate.com/recipes/134892/
# Thanks to Danny Yoo
import sys
import termios
import tty


def readchar(enter_code="\r"):
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setcbreak(sys.stdin.fileno())
        ch = sys.stdin.read(1)
        if ch in ('\r', '\n'):
            ch = enter_code
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch
