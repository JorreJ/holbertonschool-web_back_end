#!/usr/bin/env python3

"""
Function to return the floor of a floating-point number.
It removes the decimal part and returns the greatest
integer less than or equal to the number.
"""


def floor(n: float) -> int:
    """
    Returns the floor of a floating-point number using integer division.

    Parameters:
        n (float): The number to floor.

    Returns:
        int: The largest integer less than or equal to the input number.
    """
    return n // 1
