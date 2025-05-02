#!/usr/bin/env python3
"""
This script defines an asynchronous
function that uses an async list comprehension
to collect random float values from an asynchronous generator.
It demonstrates concise and efficient asynchronous data collection.
"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Asynchronously collects 10 random float values from an async generator
    using an async list comprehension.

    Returns:
        List[float]: List containing 10 random float numbers between 0 and 10.
    """
    result = [i async for i in async_generator()]
    return result
