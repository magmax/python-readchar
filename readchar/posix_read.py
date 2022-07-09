import sys
import termios
from select import select


# idea from:
# https://repolinux.wordpress.com/2012/10/09/non-blocking-read-from-stdin-in-python/
# Thanks to REPOLINUX
def _kbhit():
    return sys.stdin in select([sys.stdin], [], [], 0)[0]


# Initially taken from:
# http://code.activestate.com/recipes/134892/
# Thanks to Danny Yoo
def readchar(blocking=True):
    """Reads a single character from the input stream. Retruns None if none is avalable.
    If blocking=True the function waits for the next character."""

    ch = None

    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    term = termios.tcgetattr(fd)
    term[3] &= ~termios.ICANON & ~termios.ECHO & ~termios.IGNBRK & ~termios.BRKINT
    termios.tcsetattr(fd, termios.TCSAFLUSH, term)

    if blocking or _kbhit():
        ch = sys.stdin.read(1)

    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def readkey():
    """Get a single keypress. If an escaped key is pressed, the
    following characters are read as well (see key_linux.py)."""

    c1 = readchar()

    if c1 == "\x03":
        raise KeyboardInterrupt

    if c1 != "\x1B":
        return c1

    c2 = readchar()
    if c2 not in "\x4F\x5B":
        return c1 + c2

    c3 = readchar()
    if c3 not in "\x31\x32\x33\x35\x36":
        return c1 + c2 + c3

    c4 = readchar()
    if c4 not in "\x30\x31\x33\x34\x35\x37\x38\x39":
        return c1 + c2 + c3 + c4

    c5 = readchar()
    return c1 + c2 + c3 + c4 + c5
