from typing import List

from . import _base_key as key


class config:
    INTERRUPT_KEYS: List[str] = [key.CTRL_C]
