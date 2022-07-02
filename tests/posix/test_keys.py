from readchar import key


def test_character_length_1():
    assert 1 == len(key.CTRL_A)


def test_character_length_2():
    assert 2 == len(key.ALT_A)


def test_character_length_3():
    assert 3 == len(key.UP)


def test_character_length_4():
    assert 4 == len(key.CTRL_ALT_SUPR)
