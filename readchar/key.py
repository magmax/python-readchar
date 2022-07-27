# flake8: noqa E401,E403

from . import platform

if platform.startswith(("linux", "freebsd")):
    from ._posix_key import *
elif platform.startswith("darwin"):
    from ._posix_key import *
    from ._macos_key import *
elif platform in ("win32", "cygwin"):
    from ._win_key import *
else:
    raise NotImplementedError(f"The platform {platform} is not supported yet")
