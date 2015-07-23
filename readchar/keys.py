#These following keys are ones that have 2 meanings.
#The first key command is the one that is not in the dict below:
#ctrl_i is tab
#ctrl_[ is escape
#ctrl_2 is ctrl_c
#ctrl_h is backspace
#ctrl_j is ctrl_enter
#ctrl_m is enter

windows_special_keys = {
#Single keys:
'H': 'up',
'M': 'right',
'P': 'down',
'K': 'left',
';': 'f1',
'<': 'f2',
'=': 'f3',
'>': 'f4',
'?': 'f5',
'@': 'f6',
'A': 'f7',
'B': 'f8',
'C': 'f9',
'D': 'f10',
'S': 'delete',
#key combos
#shifted_keys
'T': 'shift_f1',
'U': 'shift_f2',
'V': 'shift_f3',
'W': 'shift_f4',
'X': 'shift_f5',
'Y': 'shift_f6',
'Z': 'shift_f7',
'[': 'shift_f8',
'\\': 'shift_f9',
']': 'shift_f10',
#ctrl_keys
'^': 'ctrl_f1',
'_': 'ctrl_f2',
'`': 'ctrl_f3',
'a': 'ctrl_f4',
'b': 'ctrl_f5',
'c': 'ctrl_f6',
'd': 'ctrl_f7',
'e': 'ctrl_f8',
'f': 'ctrl_f9',
'g': 'ctrl_f10',
'\x8d': 'ctrl_up',
'\x91': 'ctrl_down',
's': 'ctrl_left',
't': 'ctrl_right',
}

windows_keys = {
#Single keys:
'\\x1b': 'escape',
' ': 'space',
'\\x85': 'f11',
'\\x86': 'f12',
'\\x08': 'backspace',
'\\r': 'enter',
'\\t': 'tab',
#key combos
#shifted_keys
'\\x87': 'shift_f11',
'\\x88': 'shift_f12',
#ctrl_keys
'\\x89': 'ctrl_f11',
'\\x8a': 'ctrl_f12',
'\\x93': 'ctrl_delete',
'\\n': 'ctrl_enter',
'\\x94': 'ctrl_tab',
'\\x7f': 'ctrl_backspace',
'\\x1c': 'ctrl_\\',
'\\x1d': 'ctrl_]',
#ctrl letters
'\\x01': 'ctrl_a',
'\\x02': 'ctrl_b',
'\\x03': 'ctrl_c',
'\\x04': 'ctrl_d',
'\\x05': 'ctrl_e',
'\\x06': 'ctrl_f',
'\\x07': 'ctrl_g',
'\\x0b': 'ctrl_k',
'\\x0c': 'ctrl_l',
'\\x0e': 'ctrl_n',
'\\x0f': 'ctrl_o',
'\\x10': 'ctrl_p',
'\\x11': 'ctrl_q',
'\\x12': 'ctrl_r',
'\\x13': 'ctrl_s',
'\\x14': 'ctrl_t',
'\\x15': 'ctrl_u',
'\\x16': 'ctrl_v',
'\\x17': 'ctrl_w',
'\\x18': 'ctrl_x',
'\\x19': 'ctrl_y',
'\\x1a': 'ctrl_z',
'\\\\': '\\',
}