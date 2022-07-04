# flake8: noqa E401,E403

from . import platform

if (
    platform.startswith("linux")
    or platform == "darwin"
    or platform.startswith("freebsd")
):
    from .posix_key import *
elif platform in ("win32", "cygwin"):
    from .win_key import *
else:
    raise NotImplementedError(f"The platform {platform} is not supported yet")
