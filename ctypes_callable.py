# SPDX-License-Identifier: 0BSD
# Copyright 2018 Alexander Kozhevnikov <mentalisttraceur@gmail.com>


"""Implements ``callable`` using ctypes (useful on CPython 3.0 and 3.1)."""


from ctypes import py_object as _py_object
from ctypes import pythonapi as _pythonapi


__all__ = ('callable',)
__version__ = '1.0.4'


_PyCallable_Check = _pythonapi.PyCallable_Check


def callable(obj):
    """Return whether the object is callable (i.e., some kind of function).

    Note that classes are callable, as are instances of classes with a
    __call__() method.
    """
    return bool(_PyCallable_Check(_py_object(obj)))
