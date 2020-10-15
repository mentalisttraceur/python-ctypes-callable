# Copyright 2018 Alexander Kozhevnikov <mentalisttraceur@gmail.com>
#
# Permission to use, copy, modify, and distribute this software for any
# purpose with or without fee is hereby granted.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.


"""Implements ``callable`` using ctypes (useful on Python 3.0 and 3.1)

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
"""


from ctypes import py_object as _py_object
from ctypes import pythonapi as _pythonapi


__all__ = ('callable',)
__version__ = '1.0.1'


_PyCallable_Check = _pythonapi.PyCallable_Check  # pylint: disable=invalid-name


def callable(obj):  # pylint: disable=redefined-builtin
    """Return whether the object is callable (i.e., some kind of function).

    Note that classes are callable, as are instances of classes with a
    __call__() method.
    """
    return bool(_PyCallable_Check(_py_object(obj)))
