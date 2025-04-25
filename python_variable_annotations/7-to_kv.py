#!/usr/bin/env python3
from typing import Union, Tuple

"""
This script defines a function to create a tuple
containing a string and the square of a numeric value.
It uses type annotations with Union to allow both
integers and floats for the value.
"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string and a numeric value,
    and returns a tuple containing the string and
    the square of the numeric value as a float.

    Parameters:
        k (str): The string key to include in the tuple.
        v (Union[int, float]): The numeric value
        (either int or float) to be squared.

    Returns:
        Tuple[str, float]:
        A tuple where the first element is the string k,
        and the second element is the square of v as a float.
    """
    return (k, float(v**2))
