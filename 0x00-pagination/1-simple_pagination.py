#!/usr/bin/env python3
"""
Simple pagination module
"""

import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple containing a start index and an end index
    corresponding to the range of indexes to return in a list for
    the given pagination parameters.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start index and end index.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


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
            self.__dataset = dataset[1:]  # Exclude header row

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns a page of the dataset (i.e., the correct list of rows).

        Args:
            page (int): The current page number (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            List[List]: A list of rows for the given page and page size.
        """
        assert isinstance(page, int) and page > 0, "Page must be a -."
        assert isinstance(page_size, int) and page_size > 0, "Page size +."

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        # Return the slice of the dataset or an empty list if out of range
        return dataset[start_index:end_index]
