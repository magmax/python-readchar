import sys
import termios
from copy import copy
from io import StringIO
from select import select

from ._config import config


class ReadChar:
    """A ContextManager allowing for keypress collection without requiering the user to
    confirm presses with ENTER. Can be used non-blocking while inside the context."""

    def __init__(self, cfg: config = None) -> None:
        self.config = cfg if cfg is not None else config
        self._buffer = StringIO()

    def __enter__(self) -> "ReadChar":
        self.fd = sys.stdin.fileno()
        term = termios.tcgetattr(self.fd)
        self.old_settings = copy(term)

        term[3] &= ~(
            termios.ICANON  # don't require ENTER
            | termios.ECHO  # don't echo
            | termios.IGNBRK
            | termios.BRKINT
        )
        term[6][termios.VMIN] = 0  # imideatly process every input
        term[6][termios.VTIME] = 0
        termios.tcsetattr(self.fd, termios.TCSAFLUSH, term)
        return self

    def __exit__(self, type, value, traceback) -> None:
        termios.tcsetattr(self.fd, termios.TCSAFLUSH, self.old_settings)

    def __update(self) -> None:
        """check stdin and update the interal buffer if it holds data"""
        if sys.stdin in select([sys.stdin], [], [], 0)[0]:
            pos = self._buffer.tell()
            data = sys.stdin.read()
            self._buffer.write(data)
            self._buffer.seek(pos)

    @property
    def key_waiting(self) -> bool:
        """True if a key has been pressed and is waiting to be read. False if not."""
        self.__update()
        pos = self._buffer.tell()
        next_byte = self._buffer.read(1)
        self._buffer.seek(pos)
        return bool(next_byte)

    def char(self) -> str:
        """Reads a singel char from the input stream and returns it as a string of
        length one. Does not require the user to press ENTER."""
        self.__update()
        return self._buffer.read(1)

    def key(self) -> str:
        """Reads a keypress from the input stream and returns it as a string. Keypressed
        consisting of multiple characterrs will be read completly and be returned as a
        string matching the definitions in `key.py`.
        Does not require the user to press ENTER."""
        self.__update()

        c1 = self.char()
        if c1 in self.config.INTERRUPT_KEYS:
            raise KeyboardInterrupt
        if c1 != "\x1B":
            return c1
        c2 = self.char()
        if c2 not in "\x4F\x5B":
            return c1 + c2
        c3 = self.char()
        if c3 not in "\x31\x32\x33\x35\x36":
            return c1 + c2 + c3
        c4 = self.char()
        if c4 not in "\x30\x31\x33\x34\x35\x37\x38\x39":
            return c1 + c2 + c3 + c4
        c5 = self.char()
        return c1 + c2 + c3 + c4 + c5


# Initially taken from:
# http://code.activestate.com/recipes/134892/
# Thanks to Danny Yoo
# more infos from:
# https://gist.github.com/michelbl/efda48b19d3e587685e3441a74457024
# Thanks to Michel Blancard
def readchar() -> str:
    """Reads a single character from the input stream.
    Blocks until a character is available."""

    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    term = termios.tcgetattr(fd)
    try:
        term[3] &= ~(termios.ICANON | termios.ECHO | termios.IGNBRK | termios.BRKINT)
        termios.tcsetattr(fd, termios.TCSAFLUSH, term)

        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def readkey() -> str:
    """Get a keypress. If an escaped key is pressed, the full sequence is
    read and returned as noted in `_posix_key.py`."""

    c1 = readchar()

    if c1 in config.INTERRUPT_KEYS:
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
