#!/usr/bin/env python3

from typing import Tuple


def index_range(page, page_size) -> Tuple[int, int]:
    return ((page - 1) * page_size, page * page_size)