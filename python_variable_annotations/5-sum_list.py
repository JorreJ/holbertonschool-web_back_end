#!/usr/bin/env python3
from typing import List
"""
Function to calculate the sum of all float elements in a list.
Useful for aggregating numeric data from a sequence.
"""


def sum_list(input_list: List[float]) -> float:
    """
    Computes the sum of a list of floating-point numbers.

    Parameters:
        input_list (list[float]): A list of float values to be summed.

    Returns:
        float: The total sum of all elements in the input list.
    """
    n: float = 0
    for x in input_list:
        n = n + x
    return n
