import readchar


def test_readcharImport():
    assert readchar.readchar == readchar._posix_read.readchar


def test_readkeyImport():
    assert readchar.readkey == readchar._posix_read.readkey


def test_keyImport():
    a = {k: v for k, v in vars(readchar.key).items() if not k.startswith("__")}
    b = {k: v for k, v in vars(readchar._posix_key).items() if not k.startswith("__")}
    assert a == b
