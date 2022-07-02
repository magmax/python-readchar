"""Library to easily read single chars and key strokes"""

__version__ = "0.0.0-dev"
__all__ = ["readchar", "readkey", "key"]


from sys import platform


if platform.startswith("linux"):
    from .posix_read import readchar, readkey
elif platform in ("win32", "cygwin"):
    from .win_read import readchar, readkey
else:
    raise NotImplementedError(f"The platform {platform} is not supported yet")
