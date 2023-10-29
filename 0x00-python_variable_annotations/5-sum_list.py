#!/usr/bin/env python3


def sum_list(input_list: list[float]) -> float:
    total: float = 0

    for num in input_list:
        total += num

    return total
