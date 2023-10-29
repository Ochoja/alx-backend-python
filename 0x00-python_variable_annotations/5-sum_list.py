#!/usr/bin/env python3
from typing import List


def sum_list(input_list: List[float]) -> float:
    total: float = 0

    for num in input_list:
        total += num

    return total
