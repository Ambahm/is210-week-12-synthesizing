#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01 module: Custom Exception Classes"""



class BaseError(Exception):
    """A class subclassed to Esception class"""
    pass


class StringError(BaseError, TypeError):
    """ A class subclassed to BaseError and TypeError"""
    pass


class NumberError(BaseError, TypeError):
    """ A class subclassed to BaseError and TypeError"""
    pass


class NonZeroError(NumberError):
    """ A class subclassed to NumberError"""
    pass


if __name__ == '__main__':
    print issubclass(StringError, TypeError)
    print issubclass(NumberError, BaseError)
