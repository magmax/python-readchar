# -*- coding: utf-8 -*-
# Copyright (c) 2014 - 2017 Miguel Ángel García (@magmax9).

# common
TAB = '\x09'
LF = '\x0d'
CR = '\x0a'
ENTER = '\x0d'
BACKSPACE = '\x7f'
ESC = '\x1b'

# CTRL
CTRL_A = '\x01'
CTRL_B = '\x02'
CTRL_C = '\x03'
CTRL_D = '\x04'
CTRL_E = '\x05'
CTRL_F = '\x06'
CTRL_Z = '\x1a'

# ALT
ALT_A = '\x1b\x61'

# CTRL + ALT
CTRL_ALT_A = '\x1b\x01'

# cursors
UP = '\x1b\x5b\x41'
DOWN = '\x1b\x5b\x42'
LEFT = '\x1b\x5b\x44'
RIGHT = '\x1b\x5b\x43'

CTRL_ALT_SUPR = '\x1b\x5b\x33\x5e'

# other
F1 = '\x1b\x4f\x50'
F2 = '\x1b\x4f\x51'
F3 = '\x1b\x4f\x52'
F4 = '\x1b\x4f\x53'
F5 = '\x1b\x5b\x31\x35\x7e'
F6 = '\x1b\x5b\x31\x37\x7e'
F7 = '\x1b\x5b\x31\x38\x7e'
F8 = '\x1b\x5b\x31\x39\x7e'
F9 = '\x1b\x5b\x32\x30\x7e'
F10 = '\x1b\x5b\x32\x31\x7e'
F11 = '\x1b\x5b\x32\x33\x7e\x1b'
F12 = '\x1b\x5b\x32\x34\x7e\x08'

PAGE_UP = '\x1b\x5b\x35\x7e'
PAGE_DOWN = '\x1b\x5b\x36\x7e'
HOME = '\x1b\x5b\x48'
END = '\x1b\x5b\x46'

INSERT = '\x1b\x5b\x32\x7e'

# SUPR and DELETE are the same key, but for different
# keyboards (Esp. vs Eng/USA)
SUPR = '\x1b\x5b\x33\x7e'
DELETE = '\x1b\x5b\x33\x7e'

# text names for keys
KEYS = {
    CR: 'cr',
    TAB: 'tab',
    ENTER: 'enter',
    BACKSPACE: 'backspace',
    ESC: 'escape',
    UP: 'up',
    RIGHT: 'right',
    DOWN: 'down',
    LEFT: 'left',
    PAGE_UP: 'page_up',
    PAGE_DOWN: 'page_down',
    HOME: 'home',
    END: 'end',
    F1: 'f1',
    F2: 'f2',
    F3: 'f3',
    F4: 'f4',
    F5: 'f5',
    F6: 'f6',
    F7: 'f7',
    F8: 'f8',
    F9: 'f9',
    F10: 'f10',
    F11: 'f11',
    F12: 'f12',
    CTRL_A: 'ctrl_a',
    CTRL_B: 'ctrl_b',
    CTRL_C: 'ctrl_c',
    CTRL_D: 'ctrl_d',
    CTRL_E: 'ctrl_e',
    CTRL_F: 'ctrl_f',
    CTRL_Z: 'ctrl_z',
    INSERT: 'insert',
    SUPR: 'supr',
    DELETE: 'delete',
    CTRL_ALT_A: 'ctrl_alt_a'
}

windows_keys = {
    '\\x1b': ESC,
    '\\x85': F11,
    '\\x86': F12,
    '\\x08': BACKSPACE,
    '\\r': ENTER,
    '\\t': TAB,
}

windows_special_keys = {
    # Single keys:
    'H': UP,
    'M': RIGHT,
    'P': DOWN,
    'K': LEFT,
    ';': F1,
    '<': F2,
    '=': F3,
    '>': F4,
    '?': F5,
    '@': F6,
    'A': F7,
    'B': F8,
    'C': F9,
    'D': F10,
    'S': DELETE,
}

ESCAPE_SEQUENCES = (
    ESC,
    ESC + '\x5b',
    ESC + '\x5b' + '\x31',
    ESC + '\x5b' + '\x32',
    ESC + '\x5b' + '\x33',
    ESC + '\x5b' + '\x35',
    ESC + '\x5b' + '\x36',
    ESC + '\x5b' + '\x31' + '\x35',
    ESC + '\x5b' + '\x31' + '\x36',
    ESC + '\x5b' + '\x31' + '\x37',
    ESC + '\x5b' + '\x31' + '\x38',
    ESC + '\x5b' + '\x31' + '\x39',
    ESC + '\x5b' + '\x32' + '\x30',
    ESC + '\x5b' + '\x32' + '\x31',
    ESC + '\x5b' + '\x32' + '\x32',
    ESC + '\x5b' + '\x32' + '\x33',
    ESC + '\x5b' + '\x32' + '\x34',
    ESC + '\x5b' + '\x32' + '\x33' + '\x7e',
    ESC + '\x5b' + '\x32' + '\x34' + '\x7e',
    ESC + '\x4f',
    ESC + ESC,
    ESC + ESC + '\x5b',
    ESC + ESC + '\x5b' + '\x32',
    ESC + ESC + '\x5b' + '\x33',
)


def convertchar(charbuffer):
    if charbuffer in KEYS:
        return KEYS[charbuffer]
    return charbuffer
