#!/usr/bin/env python3
"""Definition of a Typed-Annotated function"""
import typing


def zoom_array(
        lst: typing.Tuple,
        factor: int = 2
        ) -> typing.List:
    """
    Takes in a 2 args and returns a Tuple
    """

    zoomed_in: typing.List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
