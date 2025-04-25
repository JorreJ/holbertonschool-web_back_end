#!/usr/bin/env python3
"""
This script defines a function to calculate
the sum of all float elements in a list.
It uses type annotations with the List type from the
typing module for better readability and type checking.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Computes the sum of a list of floating-point numbers.

    Parameters:
        input_list (List[float]): A list containing float values.

    Returns:
        float: The sum of all the float values in the list.
    """
    n: float = 0
    for x in input_list:
        n = n + x
    return n
