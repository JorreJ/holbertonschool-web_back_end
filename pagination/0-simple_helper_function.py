#!/usr/bin/env python3

"""
This script defines a utility function to compute the start and end indexes
for pagination based on the current page number and page size.
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculates the start and end index for a given page and page size.

    Parameters:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start index (inclusive)
                         and end index (exclusive) for the given pagination.
    """
    return ((page - 1) * page_size, ((page - 1) * page_size) + page_size)
