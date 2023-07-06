#!/usr/bin/env python3
"""Definition of a type-annotated function"""
import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """
    Takes list of int and floats
    sums them then returns sum as float
    """

    sum: float = 0
    for i in range(0, len(mxd_lst)):
        sum = sum + mxd_lst[i]
    return sum
