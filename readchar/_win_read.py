import msvcrt
import signal

from . import _win_key as key
from ._config import config


class ReadChar:
    """A ContextManager allowing for keypress collection without requiering the user to
    confirm presses with ENTER. Can be used non-blocking while inside the context."""

    @staticmethod
    def __silent_CTRL_C_callback(signum, frame):
        msvcrt.ungetch(key.CTRL_C.encode("ascii"))

    def __init__(self, cfg: config = None) -> None:
        self.config = cfg if cfg is not None else config

    def __enter__(self) -> "ReadChar":
        self.__org_SIGBREAK_handler = signal.getsignal(signal.SIGBREAK)
        self.__org_SIGINT_handler = signal.getsignal(signal.SIGINT)
        signal.signal(signal.SIGBREAK, signal.default_int_handler)
        signal.signal(signal.SIGINT, ReadChar.__silent_CTRL_C_callback)
        return self

    def __exit__(self, type, value, traceback) -> None:
        signal.signal(signal.SIGBREAK, self.__org_SIGBREAK_handler)
        signal.signal(signal.SIGINT, self.__org_SIGINT_handler)

    @property
    def key_waiting(self) -> bool:
        """True if a key has been pressed and is waiting to be read. False if not."""
        return msvcrt.kbhit()

    def char(self) -> str:
        """Reads a singel char from the input stream and returns it as a string of
        length one. Does not require the user to press ENTER."""
        return msvcrt.getch().decode("latin1")

    def key(self) -> str:
        """Reads a keypress from the input stream and returns it as a string. Keypressed
        consisting of multiple characterrs will be read completly and be returned as a
        string matching the definitions in `key.py`.
        Does not require the user to press ENTER."""
        c = self.char()

        if c in self.config.INTERRUPT_KEYS:
            raise KeyboardInterrupt

        # if it is a normal character:
        if c not in "\x00\xe0":
            return c

        # if it is a special key, read second half:
        return "\x00" + self.char()


def readchar() -> str:
    """Reads a single character from the input stream.
    Blocks until a character is available."""

    # manual byte decoding because some bytes in windows are not utf-8 encodable.
    return chr(int.from_bytes(msvcrt.getch(), "big"))


def readkey() -> str:
    """Reads the next keypress. If an escaped key is pressed, the full
    sequence is read and returned as noted in `_win_key.py`."""

    ch = readchar()

    if ch in config.INTERRUPT_KEYS:
        raise KeyboardInterrupt

    # if it is a normal character:
    if ch not in "\x00\xe0":
        return ch

    # if it is a scpeal key, read second half:
    ch2 = readchar()

    return "\x00" + ch2
