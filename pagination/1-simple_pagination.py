#!/usr/bin/env python3

"""
This script defines a Server class that supports pagination of a CSV dataset.
It includes a utility function to calculate index ranges for a given page and page size,
and provides methods to load the dataset and retrieve specific pages of data.
"""

import csv
import math
from typing import Tuple, List


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


class Server:
    """
    Server class to paginate a database of popular baby names.

    Attributes:
        DATA_FILE (str): The name of the CSV file containing the dataset.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        Initializes the Server instance and prepares a placeholder for the dataset.
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Loads and caches the dataset from the CSV file.

        Returns:
            List[List]: A list of rows from the CSV file, excluding the header.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieves a page of data from the dataset.

        Parameters:
            page (int): The page number to retrieve (1-indexed). Must be a positive integer.
            page_size (int): The number of items per page. Must be a positive integer.

        Returns:
            List[List]: A list of rows corresponding to the requested page.
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        dataset = self.dataset()
        first, last = index_range(page, page_size)
        return dataset[first:last]
