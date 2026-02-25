from ._base_key import *
import subprocess
import logging
import sys
module = sys.modules[__name__]


# common
BACKSPACE = "\x7f"

#there might be other key that should go here that I don't know
normal_mode = [
    "UP",
    "DOWN",
    "LEFT",
    "RIGHT",
    "END",
    "BEGIN",
    "ENTER",
    "HOME",
    "PAD_CENTER",
    "PAD_UP_DOWN",
    "PAD_UP_RIGHT",
    "PAD_DOWN_LEFT",
    "PAD_DOWN_RIGHT"
]

keys = {}  # create dico with existing key

for key in subprocess.check_output(["infocmp","-x","-1"]).decode("utf-8").split(",\n\t") :
    key = key.split( "=" )

    if len( key ) > 1 and key[0][0] == "k": # is a key and is attributed
        keys[ key[0] ] = key[1]


for key in names.keys():

    if names[ key ] not in keys.keys():# if the key is not defined
        logging.warning(f'{key} is not supported on this device')
        value = None

    else:

        if key in normal_mode:
            value = "\x1B" + "\x5B" + keys[ names[ key ] ][3:] # terminals tend to be in normal mode and termnfo give app mode

        else:
            value = "\x1B" + keys[ names[ key ] ][2:] # convert \E  to the escape sequence


    setattr( module, key, value )

del key
del value



ENTER = LF
SUPR = DELETE

