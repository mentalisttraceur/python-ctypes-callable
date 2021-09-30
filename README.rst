Python ``ctypes``-based ``callable`` reimplementation
=====================================================

Implements ``callable`` using ``ctypes`` (useful on CPython
3.0 and 3.1, which is missing the ``callable`` function).


Versioning
----------

This library's version numbers follow the `SemVer 2.0.0
specification <https://semver.org/spec/v2.0.0.html>`_.


Installation
------------

::

    pip install ctypes-callable


Usage
-----

The use-case for using this module is if:

1. You are using an **early** CPython 3 release missing ``callable``.
2. You cannot upgrade to a newer CPython 3 for some reason.
3. You want to use code which uses the ``callable`` builtin.

To do this, run this before any code that uses ``callable`` (for
example, `usercustomize` or `sitecustomize` might be good places):

.. code:: python

    import ctypes_callable
    import builtins
    builtins.callable = ctypes_callable.callable


Portability
-----------

This module will **fail** on ``import`` on Jython, IronPython, PyPy,
MicroPython, PyPy.js, Brython, Transcrypt, and probably any other
implementation besides CPython, because it relies on accessing the
Python C API through ``ctypes``.
