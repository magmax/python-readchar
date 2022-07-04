==========  =============  ===============  =======  ============
Repository    VERSION        DOWNLOADS        TESTS    COVERAGE
==========  =============  ===============  =======  ============
|github|    |pip version|  |pip downloads|  |tests|  |coveralls|
==========  =============  ===============  =======  ============

Library to easily read single chars and key-strokes.

Goal and Philosophy
===================

Born as a `python-inquirer`_ requirement.

The idea is to have a portable way to read **single** characters and **key-strokes**.


Documentation
=============

Installation
------------

.. code:: bash

   pip install readchar

The :code:`readchar` library works with python 3.6, 3.7, 3.8, 3.9 and 3.10.

Usage
-----

Usage example:

.. code:: python

  import readchar

  c = readchar.readchar()
  key = readchar.readkey()

API
---

There are just two methods:

:code:`readchar(blocking=True) -> str | None`
/////////////////////////////////////////////

Reads the next char from :code:`stdin`, returning it as a string with length 1.

By default, it will block until a character is available, but if you pass :code:`blocking=False` the function will not block and return :code:`None` if
no character is available.


:code:`readkey() -> str`
////////////////////////

Reads the next key-stroke from :code:`stdin`, returning it as a string. Waits until a key-stroke is available.

A key-stroke can be:

- single characters as returned by :code:`readchar()`. These include:

  - character for normal keys: 'a', 'z', '9'...
  - special characters like 'ENTER', 'BACKSPACE', 'TAB'...
  - combinations with CTRL

- keys that are made up of multiple characters:

  - characters for cursors/arrows: 🡩, 🡪, 🡫, 🡨
  - navigation keys: 'INSERT', 'HOME'...
  - function keys: 'f1' to 'f12'
  - for combinations with ALT: ALT+A, ...
  - combinations with CTRL and ALT: CTRL+ALT+SUPR, ...

.. attention::

  :code:`CTRL+C` will not be returned by :code:`readkey()`, but instead raise a :code:`KeyboardInterupt`. If you what to handle it yourself,
  use :code:`readchar()`.


:code:`key` module
//////////////////

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
----------

This library support both Linux and Windows, but on Windows the :code:`key` submodule has fewer keys available.

Currently unsupported, but enabled operating systems:

- macOS
- FreeBSD

Theoretically every Unix based system should work, but they will not be actively tested. It is also required that somebody provides inital testresults
before the OS is enabled and added to the list.


How to contribute
=================

You can download the code, make some changes with their tests, and make a pull-request.

In order to develop or running the tests, you can do:

1. Clone the repository.

.. code:: bash

   git clone https://github.com/magmax/python-readchar.git

2. Create a virtual environment:

.. code:: bash

   python -m venv .venv

3. Enter in the virtual environment

.. code:: bash

   source .venv/bin/activate

4. Install dependencies

.. code:: bash

    pip install -r requirements.txt

5. Install the local version of readchar (in edit mode so it automatically reflects changes)

.. code:: bash

    pip install -e .

6. Run tests

.. code:: bash

    make


Please, **Execute the tests before any pull-request**. This will avoid invalid builds.


License
=======

Copyright (c) 2014-2022 Miguel Angel Garcia (`@magmax_en`_).

Based on previous work on gist `getch()-like unbuffered character reading from stdin on both Windows and Unix (Python recipe)`_, started by `Danny Yoo`_.

Licensed under `the MIT license`_.


.. |github| image:: https://badges.aleen42.com/src/github.svg
  :target: `GitHub`_
  :alt: GitHub Repository

.. |pip version| image:: https://img.shields.io/pypi/v/readchar.svg
  :target: `pypi`_
  :alt: Latest PyPI version

.. |pip downloads| image:: https://img.shields.io/pypi/dm/readchar.svg
  :target: `pypi`_
  :alt: Number of PyPI downloads

.. |tests| image:: https://github.com/magmax/python-readchar/actions/workflows/run-tests.yml/badge.svg
  :target: https://github.com/magmax/python-readchar/actions/workflows/run-tests.yml
  :alt: Automated testing

.. |coveralls| image:: https://coveralls.io/repos/magmax/python-readchar/badge.png
  :target: https://coveralls.io/r/magmax/python-readchar
  :alt: Coveralls results

.. _pypi: https://pypi.python.org/pypi/readchar
.. _GitHub: https://github.com/magmax/python-readchar
.. _python-inquirer: https://github.com/magmax/python-inquirer
.. _@magmax_en: https://twitter.com/magmax_en

.. _the MIT license: http://opensource.org/licenses/MIT
.. _getch()-like unbuffered character reading from stdin on both Windows and Unix (Python recipe): http://code.activestate.com/recipes/134892/
.. _Danny Yoo: http://code.activestate.com/recipes/users/98032/
