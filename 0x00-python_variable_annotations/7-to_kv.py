#!/usr/bin/env python3
"""Definition of a type-annotated function"""
import typing


def to_kv(k: str, v: typing.Union[int, float]) -> tuple:
    """
    takes two args and returns a tuple
    containing the args
    """

    myTuple: typing.Tuple[typing.Union[str, float], ...] = (k, v * v)
    return myTuple
