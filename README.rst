See it at:

- `pypi`_
- `GitHub`_

==============  ===============  =========  ============
VERSION         DOWNLOADS        TESTS      COVERAGE
==============  ===============  =========  ============
|pip version|   |pip downloads|  |travis|   |coveralls|
==============  ===============  =========  ============

Library to easily read single chars and key strokes.

Goal and Philosophy
===================

Born as a `python-inquirer`_ requirement.

The idea is to have a portable way to read **single** characters and **key-strokes**.


Documentation
=============

Installation
------------

::

   pip install readchar

The :code:`readchar` library works with python 2.7, 3.4, 3.5, 3.6 and Pypy.

Usage
-----

Usage example:

.. code:: python

  import readchar

  c = readchar.readchar()
  key = readchar.readkey()

API
----

There are just two methods:

:code:`readchar()`
//////////////////

Reads the next char from :code:`stdin`, returning it as a string with length 1.


:code:`readkey()`
/////////////////

Reads the next key-stroke from :code:`stdin`, returning it as a string.

A key-stroke can have:

- 1 character for normal keys: 'a', 'z', '9'...
- 2 characters for combinations with ALT: ALT+A, ...
- 3 characters for cursors: ->, <-, ...
- 4 characters for combinations with CTRL and ALT: CTRL+ALT+SUPR, ...

There is a list of previously captured chars with their names in :code:`readchar.key`, in order to be used in comparisons and so on. This list is not enough tested and it can have mistakes, so use it carefully. Please, report them if found.


OS Support
----------

Sadly, this library has only being probed on GNU/Linux. Please, if you can try it in another OS and find a bug, put an issue or send the pull-request.

Thank you!

How to contribute
=================

You can download the code, make some changes with their tests, and make a pull-request.

In order to develop or running the tests, you can do:

1. Clone the repository.

.. code:: bash

   git clone https://github.com/magmax/python-readchar.git

2. Create a virtual environment:

.. code:: bash

   virtualenv venv

3. Enter in the virtual environment

.. code:: bash

   source venv/bin/activate

4. Install dependencies

.. code:: bash

    pip install -r requirements-test.txt

5. Run tests

.. code:: bash

    make


Please, **Execute the tests before any pull-request**. This will avoid invalid builds.


License
=======

Copyright (c) 2014-2021 Miguel Angel Garcia (`@magmax_en`_).

Based on previous work on gist `getch()-like unbuffered character reading from stdin on both Windows and Unix (Python recipe)`_, started by `Danny Yoo`_.

Licensed under `the MIT license`_.


.. |travis| image:: https://travis-ci.org/magmax/python-readchar.png
  :target: `Travis`_
  :alt: Travis results

.. |coveralls| image:: https://coveralls.io/repos/magmax/python-readchar/badge.png
  :target: `Coveralls`_
  :alt: Coveralls results_

.. |pip version| image:: https://img.shields.io/pypi/v/readchar.svg
    :target: https://pypi.python.org/pypi/readchar
    :alt: Latest PyPI version

.. |pip downloads| image:: https://img.shields.io/pypi/dm/readchar.svg
    :target: https://pypi.python.org/pypi/readchar
    :alt: Number of PyPI downloads

.. _pypi: https://pypi.python.org/pypi/readchar
.. _GitHub: https://github.com/magmax/python-readchar
.. _python-inquirer: https://github.com/magmax/python-inquirer
.. _Travis: https://travis-ci.org/magmax/python-readchar
.. _Coveralls: https://coveralls.io/r/magmax/python-readchar
.. _@magmax_en: https://twitter.com/magmax_en

.. _the MIT license: http://opensource.org/licenses/MIT
.. _getch()-like unbuffered character reading from stdin on both Windows and Unix (Python recipe): http://code.activestate.com/recipes/134892/
.. _Danny Yoo: http://code.activestate.com/recipes/users/98032/
