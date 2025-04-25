#!/usr/bin/env python3
from typing import Callable

"""
This script defines a function that returns a multiplier function.
The returned function multiplies its input by the provided multiplier.
"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a given
    number by a predefined multiplier.

    Parameters:
        multiplier (float): The multiplier to be used in the returned function.

    Returns:
        Callable[[float], float]: A function that takes a float as
        input and returns the product of the input and the multiplier.
    """
    def multiplication(n: float) -> float:
        return float(n * multiplier)

    return multiplication
