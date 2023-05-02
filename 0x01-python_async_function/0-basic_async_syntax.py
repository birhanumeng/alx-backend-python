#!/usr/bin/env python3
"""An asynchronous coroutine"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """An asyncronous function whcihc waits for random seconds \
    and returns the amount seconds it waits.
    """
    randNum = random.uniform(0, max_delay)
    await asyncio.sleep(randNum)
    return 
