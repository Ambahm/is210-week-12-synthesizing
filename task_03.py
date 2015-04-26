#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03 module"""

def exception_test(arg1, arg2, arg3):
    """Function to test exception using tuples for multiple types:
    `TypeError``, ``KeyError``, and ``IndexError``

    Args:
        caught (bool) Default set to False, for no error found.

    Returns:
        caught (bool): True if error found.

    Examples:
        >>> exception_test(['apple'], 0, 'p')
        False

        >>> exception_test(43, 1, 1)
        True

        >>> exception_test(['apple'], 0, x)
        Traceback (most recent call last):
        File "/home/vagrant/Desktop/is210-week-12-synthesizing/task_03.py",
        line 37, in <module> exception_test(['apple'], 0, x)
        NameError: name 'x' is not defined
    """

    caught = False
    try:
        arg1[arg2].index(arg3)
    except(TypeError, KeyError, IndexError): # Bundleup error types in tuple
        caught = True

    return caught


if __name__ == '__main__':
    print exception_test(['apple'], 0, 'p')
    print exception_test(43, 1, 1)
