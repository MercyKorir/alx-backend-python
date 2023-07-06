#!/usr/bin/env python3
"""Defintion of a type-annotated function"""
import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """
    Takes float as argument and returns
    a function that multiplies a float by
    multiplier variable
    """

    def multiply(x: float) -> float:
        return multiplier * x
    return multiply
