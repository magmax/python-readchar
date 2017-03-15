# -*- coding: utf-8 -*-


# common
LF = '\x0d'
CR = '\x0a'
ENTER = '\x0d'
BACKSPACE = '\x7f'
SPACE = '\x20'

ESC = '\x1b'

# Silly, but ESC key cannot be detected by itself, it must be pressed twice
# pressing the literal "Esc - [ - A" sequence on a (linux, anyway) keyboard
# is the exact same as pressing UP arrow!
ESC_KEY = ESC

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

# we can't get these because the code can't presently tell if the 5th '\x7e'
# should expect another character or not!
F11 = '\x1b\x5b\x32\x33\x7e\x1b'
F12 = '\x1b\x5b\x32\x34\x7e\x08'

PAGE_UP = '\x1b\x5b\x35\x7e'
PAGE_DOWN = '\x1b\x5b\x36\x7e'
HOME = '\x1b\x5b\x48'
END = '\x1b\x5b\x46'

INSERT = '\x1b\x5b\x32\x7e'

# what's this?  Why is it defined to '' in above Line 11?
# why is it the same as DELETE?
SUPR = '\x1b\x5b\x33\x7e'
DELETE = '\x1b\x5b\x33\x7e'

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
    ESC + '\x4f',
    ESC + ESC,
    ESC + ESC + '\x5b',
    ESC + ESC + '\x5b' + '\x32',
    ESC + ESC + '\x5b' + '\x33',
)
