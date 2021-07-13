import readchar.key
import readchar.readchar

decode_dict = {
    readchar.key.ESC: "ESC",
    readchar.key.UP: "UP",
    readchar.key.DOWN: "DOWN",
    readchar.key.LEFT: "LEFT",
    readchar.key.RIGHT: "RIGHT",
    readchar.key.PAGE_UP: "PAGE_UP",
    readchar.key.PAGE_DOWN: "PAGE_DOWN",
    readchar.key.HOME: "HOME",
    readchar.key.END: "END",
    readchar.key.INSERT: "INSERT",
    readchar.key.SUPR: "DELETE",
    readchar.key.F1: "F1",
    readchar.key.F2: "F2",
    readchar.key.F3: "F3",
    readchar.key.F4: "F4",
    readchar.key.F5: "F5",
    readchar.key.F6: "F6",
    readchar.key.F7: "F7",
    readchar.key.F8: "F8",
    readchar.key.F9: "F9",
    readchar.key.F10: "F10",
    readchar.key.F12: "F12",
    readchar.key.ALT_A: "ALT_A",
}

while True:
    c = readchar.readkey()

    if c in decode_dict:
        print("got {}".format(decode_dict[c]))
    else:
        print(c)

    if c == "d":
        break
