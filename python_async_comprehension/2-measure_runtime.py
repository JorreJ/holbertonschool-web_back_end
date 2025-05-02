#!/usr/bin/env python3
"""
This script defines an asynchronous function that measures the total runtime
of executing multiple async comprehensions concurrently using asyncio.gather.
It demonstrates the benefits of asynchronous
execution in reducing total wait time.
"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the total runtime of running four
    async_comprehension calls concurrently.

    Returns:
        float: The elapsed time in seconds to
        complete all four asynchronous tasks.
    """
    start = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    end = time.perf_counter()
    return end - start
