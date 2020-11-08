import asyncio
import os
import random
import time
from typing import Dict, Tuple


SLEEP_FROM = 10
SLEEP_TO = 100

CALCULATION_MIN = 70000
CALCULATION_MAX = 120000

COMPLETE_SCENARIO_MIN = 100
COMPLETE_SCENARIO_MAX = 1000


async def async_database_request(
    sleep_from: int = SLEEP_FROM, sleep_to: int = SLEEP_TO
) -> Dict[str, str]:
    """
    Sleeps for a random period in the interval [sleep_from, sleep_to] and returns a message.
    Remember that sleep_from and sleep_to are in milliseconds
    """
    sleep_for = random.randrange(sleep_from, sleep_to) / 1000.0
    await asyncio.sleep(sleep_for)
    return {"method": "Emulating a database call only"}


def sync_database_request(
    sleep_from: int = SLEEP_FROM, sleep_to: int = SLEEP_TO
) -> Dict[str, str]:
    """
    Sleeps for a random period in the interval [sleep_from, sleep_to] and returns a message.
    Remember that sleep_from and sleep_to are in milliseconds
    """
    sleep_for = random.randrange(sleep_from, sleep_to) / 1000.0
    time.sleep(sleep_for)
    return {"method": "Emulating a database call only"}


def do_some_calculation(
    min_size: int = CALCULATION_MIN, max_size: int = CALCULATION_MAX
) -> Dict[str, str]:
    """
    Created an array with size in the interval [min_size, max_size] with random numbers and then sorts it
    before returning a simple message.
    """
    size = random.randrange(min_size, max_size)
    arry = [random.random() for i in range(size)]
    sorted(arry)
    return {"method": "Running some important heavy calculation"}


async def async_complete_scenario(
    sleep_from: int = SLEEP_FROM,
    sleep_to: int = SLEEP_TO,
    calls_to_db: int = 2,
    min_size: int = COMPLETE_SCENARIO_MIN,
    max_size: int = COMPLETE_SCENARIO_MAX,
    calculations: int = 2,
) -> Dict[str, str]:
    """
    Runs a complete scenario by emulating the request to a database and some calculation on top
    of a supposed return from this database. This complete scenario consists of `calls_to_db` calls
    to db and `calculations` calculations.
    """
    for _ in range(calls_to_db):
        await async_database_request(sleep_from, sleep_to)
    for _ in range(calculations):
        do_some_calculation(min_size, max_size)
    return {"method": "A complete scenario just ran"}


def sync_complete_scenario(
    sleep_from: int = SLEEP_FROM,
    sleep_to: int = SLEEP_TO,
    calls_to_db: int = 2,
    min_size: int = COMPLETE_SCENARIO_MIN,
    max_size: int = COMPLETE_SCENARIO_MAX,
    calculations: int = 2,
) -> Dict[str, str]:
    """
    Runs a complete scenario by emulating the request to a database and some calculation on top
    of a supposed return from this database. This complete scenario consists of `calls_to_db` calls
    to db and `calculations` calculations.
    """
    for _ in range(calls_to_db):
        sync_database_request(sleep_from, sleep_to)
    for _ in range(calculations):
        do_some_calculation(min_size, max_size)
    return {"method": "A complete scenario just ran"}
