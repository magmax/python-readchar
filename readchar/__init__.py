"""Library to easily read single chars and key strokes"""

__version__ = "4.0.0-dev1"
__all__ = ["readchar", "readkey", "key"]

from sys import platform


if platform.startswith(("linux", "darwin", "freebsd")):
    from ._posix_read import readchar, readkey
    from . import _posix_key as key
elif platform in ("win32", "cygwin"):
    from ._win_read import readchar, readkey
    from . import _win_key as key
else:
    raise NotImplementedError(f"The platform {platform} is not supported yet")
