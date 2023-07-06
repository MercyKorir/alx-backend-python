#!/usr/bin/env python3
"""Definition of a type-annotated function"""
import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """
    takes two args and returns a tuple
    containing the args
    """

    myTuple: typing.Tuple[str, float] = (k, v * v)
    return myTuple
