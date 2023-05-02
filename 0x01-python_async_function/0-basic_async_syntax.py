#!/usr/bin/env python3
"""An asynchronous coroutine"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """An asyncronous function whcihc waits for random seconds \
    and returns the amount seconds it waits.
    """
    delay = max_delay * random.random()
    await asyncio.sleep(delay)
    return delay 
