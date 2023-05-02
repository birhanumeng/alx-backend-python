#!/usr/bin/env python3
"""An asynchronous coroutine that takes in an integer argument"""


import asyncio
import random

async def wait_random(max_delay = 10.0: float) -> float:
    """An asyncronous function whcihc waits for random seconds and return \
    it.
    """
    randNum = random.uniform(0, max_delay)
    await asyncio.sleep(randNum)
    return randNum
