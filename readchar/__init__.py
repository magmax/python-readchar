import sys


if sys.platform.startswith("linux"):
    from .read_linux import readchar, readkey
    from . import key_linux as key
elif sys.platform in ("win32", "cygwin"):
    from .read_windows import readchar, readkey
    from . import key_windows as key
else:
    raise NotImplementedError("The platform %s is not supported yet" % sys.platform)


__all__ = ["readchar", "readkey", "key"]
