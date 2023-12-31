#!/usr/bin/env python3
"""Definition of type-annotated function"""
import typing


def sum_list(input_list: typing.List[float]) -> float:
    """
    Takes a list of floating numbers,
    sums them then returns a float
    """

    sum: float = 0
    for i in range(0, len(input_list)):
        sum = sum + input_list[i]
    return sum
