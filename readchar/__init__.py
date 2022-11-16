"""Library to easily read single chars and key strokes"""

__version__ = "4.1.0-dev2"
__all__ = ["readchar", "readkey", "ReadChar", "key", "config"]

from sys import platform

from ._config import config


if platform.startswith(("linux", "darwin", "freebsd")):
    from . import _posix_key as key
    from ._posix_read import ReadChar, readchar, readkey
elif platform in ("win32", "cygwin"):
    from . import _win_key as key
    from ._win_read import ReadChar, readchar, readkey
else:
    raise NotImplementedError(f"The platform {platform} is not supported yet")
