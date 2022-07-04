| |GitHub badge| |PyPi badge| |python versions badge| |licence badge|
| |test status| |coverage status| |pip downloads badge|

python-readchar
***************

Library to easily read single chars and keystrokes.

Born as a `python-inquirer`_ requirement.


Installation
============

simply install it via :code:`pip`:

.. code:: bash

   pip install readchar

Or download the source code from PyPi_.


Usage
=====

Simply read a character or keystroke:

.. code:: python

  import readchar

  key = readchar.readkey()

React to different kinds of keypresses:

.. code:: python

  from readchar import readkey, key

  while True:
    k = readkey()
    if k == "a":
      # do stuff
    if k == key.DOWN:
      # do stuff
    if k == key.ENTER:
      break


API
===

There are just two methods:

:code:`readchar() -> str`
-------------------------

Reads one character from :code:`stdin`, returning it as a string with length 1. Waits until a character is available.

As only ASCII characters are actually a single character, you usually want to use the next function, that also handles longer keys.


:code:`readkey() -> str`
------------------------

Reads the next keystroke from :code:`stdin`, returning it as a string. Waits until a keystroke is available.

A keystroke can be:

- single characters as returned by :code:`readchar()`. These include:

  - character for normal keys: 'a', 'Z', '9',...
  - special characters like 'ENTER', 'BACKSPACE', 'TAB',...
  - combinations with 'CTRL': 'CTRL'+'A',...

- keys that are made up of multiple characters:

  - characters for cursors/arrows: 🡩, 🡪, 🡫, 🡨
  - navigation keys: 'INSERT', 'HOME',...
  - function keys: 'F1' to 'F12'
  - combinations with 'ALT': 'ALT'+'A',...
  - combinations with 'CTRL' and 'ALT': 'CTRL'+'ALT'+'SUPR',...

.. attention::

  'CTRL'+'C' will not be returned by :code:`readkey()`, but instead raise a :code:`KeyboardInterupt`. If you what to handle it yourself,
  use :code:`readchar()`.


:code:`key` module
---------------------

This submodule contains a list of available keys to compare against. The constants are defined depending on your operating system, so it should be
fully portable. If a key is listed here for your platform, :code:`readkey()` can read it and you can compare against it.


OS Support
==========

This library actively supports these operating systems:

- Linux
- Windows

Some operating systems are enabled, but not actively tested or supported:

- macOS
- FreeBSD

Theoretically every Unix based system should work, but they will not be actively tested. It is also required that somebody provides initial test
results before the OS is enabled and added to the list. Feel free to open a PR for that.

Thank you!


How to contribute
=================

You can download the code, make some changes with their tests, and open a pull-request.

In order to develop and run the tests, follow these steps:

1.  Clone the repository.

    .. code:: bash

      git clone https://github.com/magmax/python-readchar.git

2.  Create a virtual environment:

    .. code:: bash

      python -m venv .venv

3.  Enter the virtual environment

    on Linux systems:

    .. code:: bash

      source .venv/bin/activate

    or for Windows systems:

    .. code:: bash

      .venv\Scripts\activate

4.  Install dependencies

    .. code:: bash

      pip install -r requirements.txt

5.  Install the local version of readchar (in edit mode, so it automatically reflects changes)

    .. code:: bash

      pip install -e .

6.  Run tests

    .. code:: bash

      make

    (or run the command used inside the Makefile manually, if you don't have/want :code:`make`)


Please, **Execute the tests before any pull-request**. This will avoid invalid builds.


------

*Copyright (c) 2014-2022 Miguel Angel Garcia*


.. |GitHub badge| image:: https://badges.aleen42.com/src/github.svg
    :target: GitHub_
    :alt: GitHub Repository
.. |PyPi badge| image:: https://img.shields.io/pypi/v/readchar.svg
    :target: PyPi_
    :alt: Latest PyPI version
.. |Python versions badge| image:: https://img.shields.io/pypi/pyversions/readchar
    :target: PyPi_
    :alt: supported Python versions
.. |licence badge| image:: https://img.shields.io/pypi/l/readchar?color=blue
    :target: licence_
    :alt: Project licence
.. |test status| image:: https://github.com/magmax/python-readchar/actions/workflows/run-tests.yml/badge.svg?branch=master
    :target: github.com/magmax/python-readchar/actions/workflows/run-tests.yml?query=branch%3Amaster
    :alt: Automated testing results
.. |coverage status| image:: https://coveralls.io/repos/github/magmax/python-readchar/badge.svg?branch=master
    :target: https://coveralls.io/github/magmax/python-readchar?branch=master
    :alt: Coveralls results
.. |pip downloads badge| image:: https://img.shields.io/pypi/dd/readchar.svg
    :target: PyPi_
    :alt: Number of PyPI downloads

.. _GitHub: https://github.com/magmax/python-readchar
.. _PyPi: https://pypi.python.org/pypi/readchar
.. _licence: LICENCE
.. _python-inquirer: https://github.com/magmax/python-inquirer
