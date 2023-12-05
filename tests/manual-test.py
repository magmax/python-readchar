# flake8: noqa E231
from readchar import key, readkey


# construct an inverted code -> key-name mapping
# we need to revese the items so that aliases won't overrive the original name later on
known_keys = {v: k for k, v in reversed(vars(key).items()) if not k.startswith("__")}


while True:
    data = readkey()

    if data in known_keys:
        print(f"got {known_keys[data]}", end="")
    else:
        print(data, end="")

    print(" - " + "".join([f"\\x{ord(c):02x}" for c in data]))
