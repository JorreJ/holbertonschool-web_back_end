#!/usr/bin/env python3

"""
This script defines an asynchronous function that simulates a random delay.
The function waits for a random amount of time
between 0 and a specified maximum delay.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronously waits for a random amount of time between 0 and max_delay.

    Parameters:
        max_delay (int): The maximum possible delay in seconds (default is 10).

    Returns:
        float: The actual delay time in seconds.
    """
    effective_delay = random.uniform(0, max_delay)
    await asyncio.sleep(effective_delay)
    return effective_delay
