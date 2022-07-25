"""Library to easily read single chars and key strokes"""

__version__ = "4.0.0-dev1"
__all__ = ["readchar", "readkey", "key"]

from sys import platform


if (
    platform.startswith("linux")
    or platform == "darwin"
    or platform.startswith("freebsd")
):
    from ._posix_read import readchar, readkey
elif platform in ("win32", "cygwin"):
    from ._win_read import readchar, readkey
else:
    raise NotImplementedError(f"The platform {platform} is not supported yet")
