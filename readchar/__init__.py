from sys import platform


if platform.startswith("linux"):
    from .read_linux import readchar, readkey
    from . import key_linux as key
elif platform in ("win32", "cygwin"):
    from .read_windows import readchar, readkey
    from . import key_windows as key
else:
    raise NotImplementedError(f"The platform {platform} is not supported yet")


__all__ = ["readchar", "readkey", "key"]
