#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Custom exception class to offer additional functionality to debug errors"""


class CustomError(Exception):
    """Custome defined error class for error handling"""

    def __init__(self, msg, cause):
        """ Constructor to  calss Custom Error
        stores values of errors' causes
        calls in exception

        Args:
            msg(str): user defined string
            cause(str): error causes

        Returns:
           None
        """
        self.cause = cause
        self.msg = msg
        Exception.__init__(self)



if __name__ == '__main__':
    CAUSE = CustomError('Whoah!', cause='Messed up!')
    print CAUSE.msg, CAUSE.cause
