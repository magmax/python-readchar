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

`readchar()`
^^^^^^^^^^^^

Reads the next char from `stdin`, returning it as a string with length 1.


`readkey()`
^^^^^^^^^^^^

Reads the next key-stroke from `stdin`, returning it as an string.

A key-stroke can have:

- 1 character for normal keys: 'a', 'z', '9'...
- 2 characters for combinations with ALT: ALT+A, ...
- 3 characters for cursors: ->, <-, ...
- 4 characters for combinations with CTRL and ALT: CTRL+ALT+SUPR, ...

There is a list of previously captured chars with their names in `readchar.key`, in order to be used in comparations and so on. This list is not enough tested and it can have mistakes, so use it carefully. Please, report them if found.


License
=======

Copyright (c) 2014 Miguel Ángel García (`@magmax9`_).

Licensed under `the MIT license`_.


.. |travis| image:: https://travis-ci.org/magmax/python-readchar.png
  :target: `Travis`_
  :alt: Travis results

.. |coveralls| image:: https://coveralls.io/repos/magmax/python-readchar/badge.png
  :target: `Coveralls`_
  :alt: Coveralls results_

.. |pip version| image:: https://pypip.in/v/readchar/badge.png
    :target: https://pypi.python.org/pypi/readchar
    :alt: Latest PyPI version

.. |pip downloads| image:: https://pypip.in/d/readchar/badge.png
    :target: https://pypi.python.org/pypi/readchar
    :alt: Number of PyPI downloads

.. _python-inquirer: https://github.com/magmax/python-inquirer
.. _Travis: https://travis-ci.org/magmax/python-readchar
.. _Coveralls: https://coveralls.io/r/magmax/python-readchar
.. _@magmax9: https://twitter.com/magmax9

.. _the MIT license: http://opensource.org/licenses/MIT
