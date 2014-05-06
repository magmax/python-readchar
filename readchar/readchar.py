# -*- coding: utf-8 -*-
import sys


try:
    import tty
    import termios
    is_unix = True
except ImportError:
    import msvcrt
    is_unix = False


def _readchar_unix():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def _readchar_windows():
    return msvcrt.getch()


readchar = _readchar_unix if is_unix else _readchar_windows


def readkey(getchar_fn=None):
    getchar = getchar_fn or readchar
    c1 = getchar()
    if ord(c1) != 0x1b:
        return c1
    c2 = getchar()
    if ord(c2) != 0x5b:
        return c1 + c2
    c3 = getchar()
    if ord(c3) != 0x33:
        return c1 + c2 + c3
    c4 = getchar()
    return c1 + c2 + c3 + c4
