import unittest
import sys

from readchar import readkey


if sys.platform in ("win32", "cygwin"):
    import msvcrt
    from string import ascii_letters, digits, punctuation
    from readchar import key

    specialkey_dict = {
        b"\x01": key.ESC,
        b"\x1c": key.ENTER,
        b"\x3b": key.F1,
        b"\x3c": key.F2,
        b"\x3d": key.F3,
        b"\x3e": key.F4,
        b"\x3f": key.F5,
        b"\x40": key.F6,
        b"\x41": key.F7,
        b"\x42": key.F8,
        b"\x43": key.F9,
        b"\x44": key.F10,
        b"\x85": key.F11,  # only in second source
        b"\x86": key.F12,  # only in second source
        # don't have table entries for...
        # ALT_[A-Z]
        # CTRL_ALT_A, # Ctrl-Alt-A, etc.
        # CTRL_ALT_SUPR,
        # CTRL-F1
        b"\x52": key.INSERT,
        b"\x53": key.SUPR,  # key.py uses SUPR, not DELETE
        b"\x49": key.PAGE_UP,
        b"\x51": key.PAGE_DOWN,
        b"\x47": key.HOME,
        b"\x4f": key.END,
        b"\x48": key.UP,
        b"\x50": key.DOWN,
        b"\x4b": key.LEFT,
        b"\x4d": key.RIGHT
    }

    def clear_inputBuffer():
        """clear all unread characters from the inputbuffer"""
        while msvcrt.kbhit():
            msvcrt.getch()

    class ReadKeyTest(unittest.TestCase):
        def test_basic_character(self):
            """test normal characters"""
            clear_inputBuffer()
            for c in ascii_letters:
                msvcrt.ungetch(c.encode('ascii'))
                result = readkey()
                self.assertEqual(c, result)

        def test_basic_numbers(self):
            """test normal numbers"""
            clear_inputBuffer()
            for c in digits:
                msvcrt.ungetch(c.encode('ascii'))
                result = readkey()
                self.assertEqual(c, result)

        def test_basic_punctuation(self):
            """test normal punctuation/special characters"""
            clear_inputBuffer()
            for c in punctuation:
                msvcrt.ungetch(c.encode('ascii'))
                result = readkey()
                self.assertEqual(c, result)
                clear_inputBuffer()

        def test_multiple_char(self):
            """test if only one character is returned, even if two are in the inputbuffer"""
            clear_inputBuffer()
            msvcrt.ungetch(b'b')  # first keypress
            msvcrt.ungetch(b'a')  # second keypress
            result = readkey()
            self.assertEqual("b", result)

        def test_special_keys_0x00(self):
            """test if the speacial keys work, like arrow keys, ESC, F1-12 etc.
                using 0x00 as the comandbyte"""
            clear_inputBuffer()
            for c in specialkey_dict:
                msvcrt.ungetch(b'\x00')
                msvcrt.ungetch(c)
                result = readkey()
                self.assertEqual(specialkey_dict[c], result)
                clear_inputBuffer()

        def test_special_keys_0xe0(self):
            """test if the speacial keys work, like arrow keys, ESC, F1-12 etc.
                using 0xe0 as the comandbyte"""
            clear_inputBuffer()
            for c in specialkey_dict:
                msvcrt.ungetch(b'\xe0')
                msvcrt.ungetch(c)
                result = readkey()
                self.assertEqual(specialkey_dict[c], result)
                clear_inputBuffer()

else:  # Linux:
    def readchar_fn_factory(stream):

        v = [x for x in stream]

        def inner():
            return v.pop(0)

        return inner


    class ReadKeyTest(unittest.TestCase):
        def test_basic_character(self):
            getchar_fn = readchar_fn_factory("a")

            result = readkey(getchar_fn)

            self.assertEqual("a", result)

        def test_string_instead_of_char(self):
            char = "a"
            getchar_fn = readchar_fn_factory(char + "bcde")

            result = readkey(getchar_fn)

            self.assertEqual(char, result)

        def test_special_combo_character(self):
            char = "\x1b\x01"
            getchar_fn = readchar_fn_factory(char + "foo")

            result = readkey(getchar_fn)

            self.assertEqual(char, result)

        def test_special_key(self):
            char = "\x1b\x5b\x41"
            getchar_fn = readchar_fn_factory(char + "foo")

            result = readkey(getchar_fn)

            self.assertEqual(char, result)

        def test_special_key_combo(self):
            char = "\x1b\x5b\x33\x5e"
            getchar_fn = readchar_fn_factory(char + "foo")

            result = readkey(getchar_fn)

            self.assertEqual(char, result)
