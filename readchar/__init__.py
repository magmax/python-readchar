# -*- coding: utf-8 -*-
# Copyright (c) 2014 - 2017 Miguel Ángel García (@magmax9).
# Licensed under the MIT license.
# This package was inspired this gist:
# http://code.activestate.com/recipes/134892/
# A debt of gratitute belongs to DannyYoo and company.

from .readchar import readchar, readkey
from . import key

__all__ = [readchar, readkey, key]

__version__ = '0.12.0'
