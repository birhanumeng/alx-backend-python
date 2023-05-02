#!/usr/bin/env python3
"""An asynchronous coroutine"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """An asyncronous function whcihc waits for random seconds \
    and returns the amount seconds it waits.
    """
    rand_num = max_delay * random.random()
    await asyncio.sleep(rand_num)
    return rand_num
