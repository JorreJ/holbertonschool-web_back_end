#!/usr/bin/env python3

"""
This script defines a function that calculates the
length of each element in an iterable of sequences.
It returns a list of tuples, where each tuple
contains the sequence and its corresponding length.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes an iterable of sequences and returns a list of tuples,
    where each tuple contains a sequence and its length.

    Parameters:
        lst (Iterable[Sequence]): An iterable (such as a list, set,
        or any iterable) containing sequences (e.g., strings, lists, tuples).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples,
        where each tuple contains a sequence and its length.
    """
    return [(i, len(i)) for i in lst]
