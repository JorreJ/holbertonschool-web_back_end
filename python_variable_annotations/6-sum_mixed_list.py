#!/usr/bin/env python3

"""
This script defines a function to compute the sum
of a list containing both integers and floats.
It uses type annotations with Union to allow mixed
numeric types, and returns the result as a float.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Computes the sum of a list containing integers and floating-point numbers,
    and returns the result as a float.

    Parameters:
        mxd_lst (List[Union[int, float]]):
        A list containing both int and float values.

    Returns:
        float: The total sum of the elements in the list, converted to float.
    """
    return float(sum(mxd_lst))
