import sys
import termios
import tty
import select


# idea from:
# https://repolinux.wordpress.com/2012/10/09/non-blocking-read-from-stdin-in-python/
# Thanks to REPOLINUX
def kbhit():
    return sys.stdin in select.select([sys.stdin], [], [], 0)[0]


# Initially taken from:
# http://code.activestate.com/recipes/134892/
# Thanks to Danny Yoo
def readchar(blocking=True):
    """Reads a single character from the input stream. Retruns None if none is avalable.
    If blocking=True the function waits for the next character."""

    if not (blocking or kbhit()):
        return None

    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
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
    if c2 != "\x5B":
        return c1 + c2

    c3 = readchar()
    if c3 != "\x33":
        return c1 + c2 + c3

    c4 = readchar()
    return c1 + c2 + c3 + c4
