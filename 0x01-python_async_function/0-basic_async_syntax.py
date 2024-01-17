#!/usr/bin/env python3
"""Contains async coroutine"""
import random
import asyncio
from typing import Union


async def wait_random(max_delay: Union[int, float] = 10) -> int:
    """wait a random time and return same random number"""
    delay = random.uniform(0, int(max_delay))
    await asyncio.sleep(delay)
    return delay
