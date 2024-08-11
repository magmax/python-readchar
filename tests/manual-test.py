# flake8: noqa E231
from readchar import key, readkey


# construct an inverted code -> key-name mapping
# we need to revese the items so that aliases won't overrive the original name later on
known_keys = {v: k for k, v in reversed(vars(key).items()) if not k.startswith("__")}


def main():
    while True:
        read_key = readkey()
        mykey = f"got {known_keys[read_key]}" if read_key in known_keys else read_key

        print(f"{mykey} - 0x{ read_key.encode().hex() }")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt")
