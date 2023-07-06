#!/usr/bin/env python3
"""Definition of a type-annotated function"""
import typing


def element_length(
        lst: typing.Iterable[typing.Sequence]
        ) -> typing.List[typing.Tuple[typing.Sequence, int]]:
    """Takes an iterable and returns a list"""

    return [(i, len(i)) for i in lst]
