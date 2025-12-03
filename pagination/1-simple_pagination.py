#!/usr/bin/env python3
"""
This module implements simple pagination over a CSV dataset.
"""

import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """
    index_range function
    """
    return (page_size * (page - 1), page_size * page)


class Server:
    """
    Server class that loads a CSV dataset and returns paginated data.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        """Initialize the dataset cache."""
        self.__dataset: List[List[str]] | None = None

    def dataset(self) -> List[List[str]]:
        """
        Load the dataset from the CSV file if not already cached.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE, encoding="utf-8") as f:
                reader = csv.reader(f)
                data = [row for row in reader]
            self.__dataset = data[1:]  # remove header
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List[str]]:
        """
        Return the rows corresponding to a specific page.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        data = self.dataset()

        if start >= len(data):
            return []

        return data[start:end]
