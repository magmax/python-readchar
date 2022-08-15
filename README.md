[![GitHub Repository](https://badges.aleen42.com/src/github.svg)](https://github.com/magmax/python-readchar)
[![Latest PyPI version](https://img.shields.io/pypi/v/readchar.svg)](https://pypi.python.org/pypi/readchar)
[![supported Python versions](https://img.shields.io/pypi/pyversions/readchar)](https://pypi.python.org/pypi/readchar)
[![Project licence](https://img.shields.io/pypi/l/readchar?color=blue)](LICENCE) <br>
[![Automated testing results](https://github.com/magmax/python-readchar/actions/workflows/run-tests.yaml/badge.svg?branch=master)](https://github.com/magmax/python-readchar/actions/workflows/run-tests.yaml?query=branch%3Amaster)
[![Coveralls results](https://coveralls.io/repos/github/magmax/python-readchar/badge.svg?branch=master)](https://coveralls.io/github/magmax/python-readchar?branch=master)
[![Number of PyPI downloads](https://img.shields.io/pypi/dd/readchar.svg)](https://pypi.python.org/pypi/readchar)

# python-readchar

Library to easily read single chars and keystrokes.

Born as a [python-inquirer](https://github.com/magmax/python-inquirer) requirement.


## Installation

simply install it via `pip`:

```bash
pip install readchar
```

Or download the source code from [PyPi](https://pypi.python.org/pypi/readchar).


## Usage

Simply read a character or keystroke:

```python
import readchar

key = readchar.readkey()
```

React to different kinds of keypresses:

```python
from readchar import readkey, key

while True:
  k = readkey()
  if k == "a":
    # do stuff
  if k == key.DOWN:
    # do stuff
  if k == key.ENTER:
    break
```


## Documentation

There are just two methods:

### `readchar() -> str`

Reads one character from `stdin`, returning it as a string with length 1. Waits until a character is available.

As only ASCII characters are actually a single character, you usually want to use the next function, that also handles longer keys.

### `readkey() -> str`

Reads the next keystroke from `stdin`, returning it as a string. Waits
until a keystroke is available.

A keystroke can be:

- single characters as returned by `readchar()`. These include:
  - character for normal keys: <kbd>a</kbd>, <kbd>Z</kbd>, <kbd>9</kbd>,...
  - special characters like <kbd>ENTER</kbd>, <kbd>BACKSPACE</kbd>, <kbd>TAB</kbd>,...
  - combinations with <kbd>CTRL</kbd>: <kbd>CTRL</kbd>+<kbd>A</kbd>,...
- keys that are made up of multiple characters:
  - characters for cursors/arrows: <kbd>🡩</kbd>, <kbd>🡪</kbd>, <kbd>🡫</kbd>, <kbd>🡨</kbd>
  - navigation keys: <kbd>INSERT</kbd>, <kbd>HOME</kbd>,...
  - function keys: <kbd>F1</kbd> to <kbd>F12</kbd>
  - combinations with <kbd>ALT</kbd>: <kbd>ALT</kbd>+<kbd>A</kbd>,...
  - combinations with <kbd>CTRL</kbd> and <kbd>ALT</kbd>: <kbd>CTRL</kbd>+<kbd>ALT</kbd>+<kbd>SUPR</kbd>,...

> **Note**
> <kbd>CTRL</kbd>+<kbd>C</kbd> will not be returned by `readkey()`, but instead raise a `KeyboardInterupt`. If you what to handle it yourself, use `readchar()`.

### `readchar.key` module

This submodule contains a list of available keys to compare against. The constants are defined depending on your operating system, so it should be
fully portable. If a key is listed here for your platform, `readkey()` can read it, and you can compare against it.


## OS Support

This library actively supports these operating systems:

- Linux
- Windows

Some operating systems are enabled, but not actively tested or supported:

- macOS
- FreeBSD

Theoretically every Unix based system should work, but they will not be actively tested. It is also required that somebody provides initial test
results before the OS is enabled and added to the list. Feel free to open a PR for that.

Thank you!


## How to contribute

You have an issue problem or found a bug? You have a great new idea or just want to fix a typo? Great :+1:. We are happy to accept your issue or pull
request, but first, please read our [contribution guidelines](https://github.com/magmax/python-readchar/blob/master/CONTRIBUTING.md). They will also
tell you how to write code for this repo and how to properly prepare an issue or a pull request.

-----

*Copyright (c) 2014-2022 Miguel Ángel García*