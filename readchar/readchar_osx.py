# -*- coding: utf-8 -*-
# Initially taken from:
# http://code.activestate.com/recipes/users/1166064/
import Carbon


def readchar():
    key_down_mask = 0x0008
    if Carbon.Evt.EventAvail(key_down_mask)[0] == 0:
        return ''
    #
    # The event contains the following info:
    # (what,msg,when,where,mod)=Carbon.Evt.GetNextEvent(0x0008)[1]
    #
    # The message (msg) contains the ASCII char which is
    # extracted with the 0x000000FF charCodeMask; this
    # number is converted to an ASCII character with chr() and
    # returned
    #
    (what, msg, when, where, mod) = Carbon.Evt.GetNextEvent(0x0008)[1]
    return chr(msg & 0x000000FF)
