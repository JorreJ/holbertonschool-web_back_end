#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination

This script defines a Server class that supports pagination over a dataset,
even if entries are deleted between requests. It provides methods to access
both the raw and indexed datasets, and to paginate using a stable indexing
system.
"""

import csv
import math
from typing import List, Dict


class Server:
    """
    Server class to paginate a database of popular baby names.

    Attributes:
        DATA_FILE (str): Path to the CSV file containing the dataset.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        Initializes the Server with placeholders
        for the dataset and its indexed version.
        """
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """
        Loads and caches the dataset from the CSV file.

        Returns:
            List[List]: A list of rows from the dataset, excluding the header.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Creates and caches an indexed version of the dataset.

        The dataset is stored in a dictionary where keys are index positions,
        allowing for deletion-resilient access.

        Returns:
            Dict[int, List]: A dictionary mapping index to dataset row.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Returns a page of the dataset starting from
        the given index with pagination metadata.

        This method is resilient to deletions:
        it skips missing indices and continues until the
        page_size is met or the dataset is exhausted.

        Parameters:
            index (int): The starting index from which to return data.
            page_size (int): The number of items to return.

        Returns:
            Dict: A dictionary containing:
                - index (int): The starting index of the page.
                - next_index (int): The index to use in the next call.
                - page_size (int): The number of items returned.
                - data (List): The actual page data.
        """
        assert isinstance(index, int) and index >= 0
        indexed_data = self.indexed_dataset()
        assert index < len(indexed_data)

        data = []
        current_index = index
        count = 0

        while count < page_size and\
                current_index < len(self.__dataset) + page_size:
            item = indexed_data.get(current_index)
            if item:
                data.append(item)
                count += 1
            current_index += 1

        return {
            'index': index,
            'next_index': current_index,
            'page_size': len(data),
            'data': data
        }
