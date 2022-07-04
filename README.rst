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

or download the source code from PyPi_.


Usage
=====

Usage example:

.. code:: python

  import readchar

  c = readchar.readchar()
  key = readchar.readkey()

API
===

There are just two methods:

:code:`readchar(blocking=True) -> str | None`
---------------------------------------------

Reads the next char from :code:`stdin`, returning it as a string with length 1.

By default, it will block until a character is available, but if you pass :code:`blocking=False` the function will not block and return :code:`None`
if no character is available.


:code:`readkey() -> str`
------------------------

Reads the next keystroke from :code:`stdin`, returning it as a string. Waits until a keystroke is available.

A keystroke can be:

- single characters as returned by :code:`readchar()`. These include:

  - character for normal keys: 'a', 'Z', '9'...
  - special characters like 'ENTER', 'BACKSPACE', 'TAB'...
  - combinations with 'CTRL': 'CTRL'+'A',...

- keys that are made up of multiple characters:

  - characters for cursors/arrows: 🡩, 🡪, 🡫, 🡨
  - navigation keys: 'INSERT', 'HOME',...
  - function keys: 'F1' to 'F12'
  - combinations with 'ALT': 'ALT'+'A',...
  - combinations with 'CTRL' and 'ALT': 'CTRL'+'ALT'+'SUPR',...

.. attention::

  'CTRL'+'C' will not be returned by :code:`readkey()`, but instead raise a :code:`KeyboardInterupt`. If you what to handle it yourself,
  use :code:`readchar()`. Also note that using the none-blocking version may result in unexpected behaviour for :code:`KeyboardInterupt`.


:code:`key.py` module
---------------------

This submodule contains a list of available keys to compare against. You can use it like this:

.. code:: python

  from readchar import readkey, key

  while True:
    k = readkey()
    if k == key.UP:
      # do stuff
    if k == key.DOWN:
      # do stuff
    if k == key.ENTER:
      # do stuff


OS Support
==========

This library support both Linux and Windows, but on Windows the :code:`key` submodule has fewer keys available.

Currently unsupported, but enabled operating systems:

- macOS
- FreeBSD

Theoretically every Unix based system should work, but they will not be actively tested. It is also required that somebody provides initial test
results before the OS is enabled and added to the list. Feel free to open a PR for that.

Thank you!


How to contribute
=================

You can download the code, make some changes with their tests, and open a pull-request.

In order to develop and run the tests, follow these steps:

1. Clone the repository.

.. code:: bash

   git clone https://github.com/magmax/python-readchar.git

2. Create a virtual environment:

.. code:: bash

   python -m venv .venv

3. Enter the virtual environment

.. code:: bash

   source .venv/bin/activate

4. Install dependencies

.. code:: bash

    pip install -r requirements.txt

5. Install the local version of readchar (in edit mode, so it automatically reflects changes)

.. code:: bash

    pip install -e .

6. Run tests

.. code:: bash

    make


Please, **Execute the tests before any pull-request**. This will avoid invalid builds.


Licence
=======

Copyright (c) 2014-2022 Miguel Angel Garcia (`@magmax_en`_).

Based on previous work on gist `getch()-like unbuffered character reading from stdin on both Windows and Unix (Python recipe)
<https://code.activestate.com/recipes/134892/>`_, started by Danny Yoo as well as gist
`kbhit.py <https://gist.github.com/michelbl/efda48b19d3e587685e3441a74457024>`_ by Michel Blancard.

Licensed under `the MIT licence <licence_>`_.


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
.. |test status| image:: https://github.com/magmax/python-readchar/actions/workflows/run-tests.yml/badge.svg
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
.. _@magmax_en: https://twitter.com/magmax_en
