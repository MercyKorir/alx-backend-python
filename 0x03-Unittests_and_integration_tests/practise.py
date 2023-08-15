#!/usr/bin/env python3
from utils import access_nested_map

nested_map = {
    'a': {
        'b': {
            'c': 1
        }
    },
    'd': 2
}

valuec = access_nested_map(nested_map, ['a', 'b', 'c'])
valued = access_nested_map(nested_map, ['d'])
valueb = access_nested_map(nested_map, ['a', 'b'])
valuea = access_nested_map(nested_map, ['a'])
valuee = access_nested_map(nested_map, ['e'])
print("c: {}".format(valuec))
print("d: {}".format(valued))
print("b: {}".format(valueb))
print("a: {}".format(valuea))
print("e: {}".format(valuee))

