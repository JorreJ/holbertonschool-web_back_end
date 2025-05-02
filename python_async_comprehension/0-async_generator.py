#!/usr/bin/env python3
"""
This script defines an asynchronous generator
function that yields random float values.
It simulates a data stream by introducing a delay between each value.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronously yields 10 random float numbers between 0 and 10,
    with a 1-second pause between each.

    Yields:
        float: A random float number between 0 and 10.
    """
    for x in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
