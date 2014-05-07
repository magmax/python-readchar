# -*- coding: utf-8 -*-
# Initially taken from:
# http://code.activestate.com/recipes/users/1166064/
import Carbon

def readchar():
    if Carbon.Evt.EventAvail(0x0008)[0]==0: # 0x0008 is the keyDownMask
        return ''
    else:
        #
        # The event contains the following info:
        # (what,msg,when,where,mod)=Carbon.Evt.GetNextEvent(0x0008)[1]
        #
        # The message (msg) contains the ASCII char which is
        # extracted with the 0x000000FF charCodeMask; this
        # number is converted to an ASCII character with chr() and
        # returned
        #
        (what,msg,when,where,mod)=Carbon.Evt.GetNextEvent(0x0008)[1]
        return chr(msg &amp; 0x000000FF)
