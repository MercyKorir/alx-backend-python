#!/usr/bin/env python3
"""Definition of a duck-typed annotation function"""
import typing


def safe_first_element(
        lst: typing.Sequence[typing.Any]
        ) -> typing.Optional[typing.Any]:
    """
    Takes list and returns either Any type
    or None
    """

    if lst:
        return lst[0]
    else:
        return None
