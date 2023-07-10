#!/usr/bin/env python3
"""definition of a type-annotated function"""


def safely_get_value(dct, key, default = None):
    if key in dict:
        return dct[key]
    else:
        return default
