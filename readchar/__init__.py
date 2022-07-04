"""Library to easily read single chars and key strokes"""

__version__ = "0.0.0-dev"


from . import key
from .readchar import readchar, readkey

__all__ = [readchar, readkey, key]
