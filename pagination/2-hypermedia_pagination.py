#!/usr/bin/env python3

import csv
import math
from typing import Tuple, List, Dict


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
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
            assert isinstance(page, int) and isinstance(page_size, int)
            assert page > 0 and page_size > 0
            dataset = self.dataset()
            first, last = index_range(page, page_size)
            return dataset[first:last]
    
    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        data = self.get_page(page, page_size)
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)

        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if (page + 1) <= total_pages else None,
            'prev_page': page - 1 if (page - 1) > 0 else None,
            'total_pages': total_pages
        }