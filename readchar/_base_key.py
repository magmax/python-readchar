# common
LF = "\x0a"
CR = "\x0d"
SPACE = "\x20"
ESC = "\x1b"
TAB = "\x09"

# CTRL
CTRL_A = "\x01"
CTRL_B = "\x02"
CTRL_C = "\x03"
CTRL_D = "\x04"
CTRL_E = "\x05"
CTRL_F = "\x06"
CTRL_G = "\x07"
CTRL_H = "\x08"
CTRL_I = TAB
CTRL_J = LF
CTRL_K = "\x0b"
CTRL_L = "\x0c"
CTRL_M = CR
CTRL_N = "\x0e"
CTRL_O = "\x0f"
CTRL_P = "\x10"
CTRL_Q = "\x11"
CTRL_R = "\x12"
CTRL_S = "\x13"
CTRL_T = "\x14"
CTRL_U = "\x15"
CTRL_V = "\x16"
CTRL_W = "\x17"
CTRL_X = "\x18"
CTRL_Y = "\x19"
CTRL_Z = "\x1a"

names = {
    "ESC"                : "kbs",        #backslash key ?
    "BEGIN"              : "kbeg",       #begin key
    "CLEAR_ALL_TAB"      : "ktbc",       #clear-all-tabs key
    "CLEAR"              : "kclr",       #clear-screen or erase key
    "CLEAR_TAB"          : "kctab",      #clear-tab key
    "BACK_TAB"           : "kcbt",       #back tab key
    "ENTER"              : "kent",       #enter key
    "DELETE"             : "kdch1",      #delete-character key
    "DELETE_LINE"        : "kdl1",       #delete-line key
    "END"                : "kend",       #end key
    "END_OF_LINE"        : "kel",        #clear-to-end-of-line key
    "END_OF_SCREEN"      : "ked",        #clear-to-end-of-screen key
    "HOME"               : "khome",      #home key
    "INSERT"             : "kich1",      #insert-character key
    "INSERT_LINE"        : "kil1",       #insert-line key
    "HOME_DOWN"          : "kll",        #lower-left key (home down)
    "PAGE_UP"            : "kpp",        #up page key
    "PAGE_DOWN"          : "knp",        #down page key
    "SCROLL_FORWARD"     : "kind",       #scroll-forward key
    "SCROLL_BACKWARD"    : "kri",        #scroll-backward key
    "SET_TAB"            : "khts",       #set-tab key
    "RIGHT"              : "kcuf1",      #right-arrow key
    "LEFT"               : "kcub1",      #left-arrow key
    "UP"                 : "kcuu1",      # up arrow key
    "DOWN"               : "kcud1",      # down-arrow key

    "PAD_UP_DOWN"        : "ka1",        #upper left of keypad
    "PAD_UP_RIGHT"       : "ka3",        #upper right of keypad
    "PAD_CENTER"         : "kb2",        #center of keypad
    "PAD_DOWN_LEFT"      : "kc1",        #lower left of keypad
    "PAD_DOWN_RIGHT"     : "kc3",        #lower right of keypad

    "SHIFT_EXIT"         : "kEXT",       #shifted exit key
    "SHIFT_FIND"         : "kFND",       #shifted find key
    "SHIFT_HELP"         : "kHLP",       #shifted help key
    "SHIFT_HOME"         : "kHOM",       #shifted home key
    "SHIFT_INSERT"       : "kIC",        #shifted insert-character key
    "SHIFT_LEFT"         : "kLFT",       #shifted left-arrow key
    "SHIFT_RIGHT"        : "kRIT",       #shifted right-arrow key
    "SHIFT_MESSAGE"      : "kMSG",       #shifted message key
    "SHIFT_MOVE"         : "kMOV",       #shifted move key
    "SHIFT_NEXT"         : "kNXT",       #shifted next key
    "SHIFT_OPTIONS"      : "kOPT",       #shifted options key
    "SHIFT_PREVIOUS"     : "kPRV",       #shifted previous key
    "SHIFT_PRINT"        : "kPRT",       #shifted print key
    "SHIFT_REDO"         : "kRDO",       #shifted redo key
    "SHIFT_REPLACE"      : "kRPL",       #shifted replace key
    "SHIFT_RESUME"       : "kRES",       #shifted resume key
    "SHIFT_SAVE"         : "kSAV",       #shifted save key
    "SHIFT_SUSPEND"      : "kSPD",       #shifted suspend key
    "SHIFT_UNDO"         : "kUND",       #shifted undo key
    "SHIFT_DELETE_LINE"  : "kDL",        #shifted delete line
    "SHIFT_DELETE"       : "kDC",        #shifted delete chracter
    "SHIFT_END"          : "kEND",       #shifted end key

    "F0"                 : "kf0",        #F0 function key
    "F1"                 : "kf1",        #F1 function key
    "F2"                 : "kf2",        #F2 function key
    "F3"                 : "kf3",        #F3 function key
    "F4"                 : "kf4",        #F4 function key
    "F5"                 : "kf5",        #F5 function key
    "F6"                 : "kf6",        #F6 function key
    "F7"                 : "kf7",        #F7 function key
    "F8"                 : "kf8",        #F8 function key
    "F9"                 : "kf9",        #F9 function key
    "F10"                : "kf10",       #F10 function key
    "F11"                : "kf11",       #F11 function key
    "F12"                : "kf12",       #F12 function key

    "F13"                : "kf13",       #F13 function key
    "F14"                : "kf14",       #F14 function key
    "F15"                : "kf15",       #F15 function key
    "F16"                : "kf16",       #F16 function key
    "F17"                : "kf17",       #F17 function key
    "F18"                : "kf18",       #F18 function key
    "F19"                : "kf19",       #F19 function key
    "F20"                : "kf20",       #F20 function key
    "F21"                : "kf21",       #F21 function key
    "F22"                : "kf22",       #F22 function key
    "F23"                : "kf23",       #F23 function key
    "F24"                : "kf24",       #F24 function key
    "F25"                : "kf25",       #F25 function key

    "F26"                : "kf26",       #F26 function key
    "F27"                : "kf27",       #F27 function key
    "F28"                : "kf28",       #F28 function key
    "F29"                : "kf29",       #F29 function key
    "F30"                : "kf30",       #F30 function key
    "F31"                : "kf31",       #F31 function key
    "F32"                : "kf32",       #F32 function key
    "F33"                : "kf33",       #F33 function key
    "F34"                : "kf34",       #F34 function key
    "F35"                : "kf35",       #F35 function key
    "F36"                : "kf36",       #F36 function key
    "F37"                : "kf37",       #F37 function key
    "F38"                : "kf38",       #F38 function key

    "F39"                : "kf39",       #F39 function key
    "F40"                : "kf40",       #F40 function key
    "F41"                : "kf41",       #F41 function key
    "F42"                : "kf42",       #F42 function key
    "F43"                : "kf43",       #F43 function key
    "F44"                : "kf44",       #F44 function key
    "F45"                : "kf45",       #F45 function key
    "F46"                : "kf46",       #F46 function key
    "F47"                : "kf47",       #F47 function key
    "F48"                : "kf48",       #F48 function key
    "F49"                : "kf49",       #F49 function key
    "F50"                : "kf50",       #F50 function key
    "F51"                : "kf51",       #F51 function key

    "F52"                : "kf52",       #F52 function key
    "F53"                : "kf53",       #F53 function key
    "F54"                : "kf54",       #F54 function key
    "F55"                : "kf55",       #F55 function key
    "F56"                : "kf56",       #F56 function key
    "F57"                : "kf57",       #F57 function key
    "F58"                : "kf58",       #F58 function key
    "F59"                : "kf59",       #F59 function key
    "F60"                : "kf60",       #F60 function key
    "F61"                : "kf61",       #F61 function key
    "F62"                : "kf62",       #F62 function key
    "F63"                : "kf63",       #F63 function key


    #from here its user defined with standards names

    "ALT_DELETE"             : "kDC3",
    "ALT_SHIFT_DELETE"       : "kDC4",
    "CONTROL_DELETE"         : "kDC5",
    "CONTROL_SHIFT_DELETE"   : "kDC6",
    "ALT_CONTROL_DELETE"     : "kDC7",

    "SHIFT_DOWN"             : "kDN",
    "ALT_DOWN"               : "kDN3",
    "ALT_SHIFT_DOWN"         : "kDN4",
    "CONTROL_DOWN"           : "kDN5",
    "SHIFT_CONTROL_DOWN"     : "kDN6",
    "ALT_CONTROL_DOWN"       : "kDN7",

    "SHIFT_UP"               : "kUP",
    "ALT_UP"                 : "kUP3",
    "ALT_SHIFT_UP"           : "kUP4",
    "CONTROL_UP"             : "kUP5",
    "CONTROL_SHIFT_UP"       : "kUP6",
    "ALT_CONTROL_UP"         : "kUP7",

    "ALT_LEFT"               : "kLFT3",
    "ALT_SHIFT_LEFT"         : "kLFT4",
    "CONTROL_LEFT"           : "kLFT5",
    "CONTROL_SHIFT_LEFT"     : "kLFT6",
    "ALT_CONTROL_LEFT"       : "kLFT7",

    "ALT_RIGHT"              : "kRIT3",
    "ALT_SHIFT_RIGHT"        : "kRIT4",
    "CONTROL_RIGHT"          : "kRIT5",
    "CONTROL_SHIFT_RIGHT"    : "kRIT6",
    "ALT_CONTROL_RIGHT"      : "kRIT7",

    "ALT_END"                : "kEND3",
    "ALT_SHIFT_END"          : "kEND4",
    "CONTROL_END"            : "kEND5",
    "CONTROL_SHIFT_END"      : "kEND6",
    "ALT_CONTROL_END"        : "kEND7",

    "ALT_HOME"               : "kHOM3",
    "ALT_SHIFT_HOME"         : "kHOM4",
    "CONTROL_HOME"           : "kHOM5",
    "CONTROL_SHIFT_HOME"     : "kHOM6",
    "ALT_CONTROL_HOME"       : "kHOM7",

    "ALT_INSERT"             : "kIC3",
    "ALT_SHIFT_INSERT"       : "kIC4",
    "CONTROL_INSERT"         : "kIC5",
    "CONTROL_SHIFT_INSERT"   : "kIC6",
    "ALT_CONTROL_INSERT"     : "kIC7",

    "ALT_NEXT"               : "kNXT3",
    "ALT_SHIFT_NEXT"         : "kNXT4",
    "CONTROL_NEXT"           : "kNXT5",
    "CONTROL_SHIFT_NEXT"     : "kNXT6",
    "ALT_CONTROL_NEXT"       : "kNXT7",

    "ALT_PREVIOUS"           : "kPRV3",
    "ALT_SHIFT_PREVIOUS"     : "kPRV4",
    "CONTROL_PREVIOUS"       : "kPRV5",
    "CONTROL_SHIFT_PREVIOUS" : "kPRV6",
    "ALT_CONTROL_PREVIOUS"   : "kPRV7"
}




#list of possible keys

