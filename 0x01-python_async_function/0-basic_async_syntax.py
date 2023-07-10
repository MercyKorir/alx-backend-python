#!/usr/bin/env python3
"""Definition of an asynchronous coroutine"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Takes int arg, waits for a random delay,
    and returns it
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)

    return delay
