#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    try:
        value = int(value)
    except ValueError as err:
        sys.stderr.write("Exception: {}".format(err))
        return False
    else:
        print("{:d}".format(value))
        return True
