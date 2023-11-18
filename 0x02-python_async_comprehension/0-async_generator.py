#!/usr/bin/env python3
"""An async generator"""
import asyncio
import random


async def async_generator():
    """Returns a generator"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
