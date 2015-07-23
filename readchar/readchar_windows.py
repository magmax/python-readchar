# -*- coding: utf-8 -*-
# Initially taken from:
# http://code.activestate.com/recipes/134892/#c9
# Thanks to Stephen Chappell
import msvcrt
from keys import windows_keys, windows_special_keys

def readchar(blocking=False):
	"""Get a single character on Windows."""
	ch = msvcrt.getch()
	if ch in '\x00\xe0':
		ch = msvcrt.getch()
		ch = windows_special_keys.get(ch, ch)
	ch = repr(ch)[1:-1]
	if ch.startswith('\\') or ch == ' ':
		ch = windows_keys.get(ch, ch)
	return ch

if __name__ == '__main__':
	while True:
		c = readchar()
		print(c)

		if c == 'e':
			break
