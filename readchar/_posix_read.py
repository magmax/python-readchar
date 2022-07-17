import sys
import termios
import tty


# Initially taken from:
# http://code.activestate.com/recipes/134892/
# Thanks to Danny Yoo
def readchar() -> str:
    """Reads a single character from the input stream.
    Blocks until a character is available."""

    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def readkey(getchar_fn=None):
    getchar = getchar_fn or readchar
    c1 = getchar()
    if ord(c1) != 0x1B:
        return c1
    c2 = getchar()
    if ord(c2) != 0x5B:
        return c1 + c2
    c3 = getchar()
    if ord(c3) != 0x33:
        return c1 + c2 + c3
    c4 = getchar()
    return c1 + c2 + c3 + c4
