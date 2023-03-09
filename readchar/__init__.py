"""Library to easily read single chars and key strokes"""

__version__ = "4.0.4-dev3"
__all__ = ["readchar", "readkey", "key", "config"]

from sys import platform

from ._config import config


if platform.startswith(("linux", "darwin", "freebsd")):
    from . import _posix_key as key
    from ._posix_read import readchar, readkey
elif platform in ("win32", "cygwin"):
    from . import _win_key as key
    from ._win_read import readchar, readkey
else:
    raise NotImplementedError(f"The platform {platform} is not supported yet")
