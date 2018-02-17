Python ``ctypes``-based ``callable`` reimplementation
=====================================================

Implements ``callable`` using ctypes (useful on Python 3.0 and 3.1)

Most Python versions have a native builtin function called ``callable``
which checks if the argument is a callable object.

Python 3 initially removed the builtin function (but kept the internal
C function), before adding it back in Python 3.2 because no alternative
is truly equivalent in all cases.

This module provides a function named ``callable`` which is equivalent
to the native ``callable``, by directly accessing the underlying CPython
API through the ``ctypes`` module.

This isn't very useful by itself for most Python versions, but it is an
essential building block for enabling code relying on ``callable`` to
work on Python 3.0 and 3.1.


Versioning
----------

This library's version numbers follow the `SemVer 2.0.0 specification
<https://semver.org/spec/v2.0.0.html>`_.

The current version number is available in the variable ``__version__``
as is normal for Python modules.


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

This module relies on accessing the Python C API through `ctypes`, which
means it will fail on import on Jython, IronPython, PyPy, MicroPython,
PyPy.js, Brython, Transcrypt, and probably every other implementation
besides CPython.

If you're looking for something that's basically this, but won't break
upon import on other Python implementations, you can use
`the ``polyfill-callable`` module
<https://github.com/mentalisttraceur/python-polyfill-callable>`_ instead.
