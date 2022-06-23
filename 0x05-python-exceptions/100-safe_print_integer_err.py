#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    try:
        if not value.isdigit() and isinstance(value, str):
            return False
        x = int(value)
        print("{:d}".format(x))
        return True
    except Exception as e:
        sys.stderr.write("Exception: {}".format(e))
        return False
