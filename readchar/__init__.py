# -*- coding: utf-8 -*-
# This file is based on this gist:
# http://code.activestate.com/recipes/134892/
# So real authors are DannyYoo and company.

from .readchar import readchar, readkey
from . import key

__all__ = [readchar, readkey, key]

__version__ = '0.0.8'
