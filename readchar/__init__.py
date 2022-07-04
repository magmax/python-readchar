"""Library to easily read single chars and key strokes"""

__version__ = "4.0.0-dev0"


from . import key
from .readchar import readchar, readkey

__all__ = [readchar, readkey, key]
