# -*- coding: utf-8 -*-
# Copyright (c) 2014, 2015 Miguel Ángel García (@magmax9).
# Based on previous work on gist getch()-like unbuffered character
# reading from stdin on both Windows and Unix (Python recipe),
# started by Danny Yoo. Licensed under the MIT license.

# common
LF = '\x0d'
CR = '\x0a'
ENTER = '\x0d'
BACKSPACE = '\x7f'
ESC = '\x1b'
TAB = '\x09'

# CTRL
CTRL_A = '\x01'
CTRL_B = '\x02'
CTRL_C = '\x03'
CTRL_D = '\x04'
CTRL_E = '\x05'
CTRL_F = '\x06'
CTRL_Z = '\x1a'

LEFTBRACKET = '\x5b'

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
F5 = '\x1b\x4f\x31\x35\x7e'
F6 = '\x1b\x4f\x31\x37\x7e'
F7 = '\x1b\x4f\x31\x38\x7e'
F8 = '\x1b\x4f\x31\x39\x7e'
F9 = '\x1b\x4f\x32\x30\x7e'
F10 = '\x1b\x4f\x32\x31\x7e'
F11 = '\x1b\x4f\x32\x33\x7e'
F12 = '\x1b\x4f\x32\x34\x7e'

PAGE_UP = '\x1b\x5b\x35\x7e'
PAGE_DOWN = '\x1b\x5b\x36\x7e'
HOME = '\x1b\x5b\x48'
END = '\x1b\x5b\x46'

INSERT = '\x1b\x5b\x32\x7e'
DELETE = '\x1b\x5b\x33\x7e'

ESCAPE_SEQUENCES = (
    ESC,
    ESC + LEFTBRACKET,
    ESC + LEFTBRACKET + '\x31',
    ESC + LEFTBRACKET + '\x32',
    ESC + LEFTBRACKET + '\x33',
    ESC + LEFTBRACKET + '\x35',
    ESC + LEFTBRACKET + '\x36',
    ESC + LEFTBRACKET + '\x31' + '\x35',
    ESC + LEFTBRACKET + '\x31' + '\x36',
    ESC + LEFTBRACKET + '\x31' + '\x37',
    ESC + LEFTBRACKET + '\x31' + '\x38',
    ESC + LEFTBRACKET + '\x31' + '\x39',
    ESC + LEFTBRACKET + '\x32' + '\x30',
    ESC + LEFTBRACKET + '\x32' + '\x31',
    ESC + LEFTBRACKET + '\x32' + '\x32',
    ESC + LEFTBRACKET + '\x32' + '\x33',
    ESC + LEFTBRACKET + '\x32' + '\x34',
    ESC + '\x4f',
    ESC + ESC,
    ESC + ESC + LEFTBRACKET,
    ESC + ESC + LEFTBRACKET + '\x32',
    ESC + ESC + LEFTBRACKET + '\x33',
)

linux_keys = {
    # Single keys:
    CR: 'cr',
    ENTER: 'enter',
    BACKSPACE: 'backspace',
    ESC: 'escape',
    HOME: "home",
    UP: 'up',
    TAB: 'tab',
    RIGHT: 'right',
    DOWN: 'down',
    LEFT: 'left',
    PAGE_UP: 'page_up',
    PAGE_DOWN: 'page_down',
    END: "end",
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
    DELETE: 'delete',
    CTRL_A: 'ctrl_a',
    CTRL_B: 'ctrl_b',
    CTRL_C: 'ctrl_c',
    CTRL_D: 'ctrl_d',
    CTRL_E: 'ctrl_e',
    CTRL_F: 'ctrl_f',
    CTRL_Z: 'ctrl_z',
    INSERT: 'insert',
    CTRL_ALT_A: 'ctrl_alt_a'
}
