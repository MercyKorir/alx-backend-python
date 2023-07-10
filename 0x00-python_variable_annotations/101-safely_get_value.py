#!/usr/bin/env python3
"""definition of a type-annotated function"""
import typing

T = typing.TypeVar('T')


def safely_get_value(
        dct: typing.Mapping,
        key: typing.Any,
        default: typing.Union[T, None] = None) -> typing.Union[typing.Any, T]:
    """
    takes in parameters and returns values
    """

    if key in dict:
        return dct[key]
    else:
        return default
