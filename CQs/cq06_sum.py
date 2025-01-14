"""summing the elemnts of a list using different loops"""

__author__ = "730760282"


def w_sum(vals: list[float]) -> float:
    i = 0
    sum = 0
    while i < len(vals):
        sum += vals[i]
        i += 1
    return sum


def f_sum(vals: list[float]) -> float:
    sum = 0
    for elem in vals:
        sum += elem
    return sum


def f_range_sum(vals: list[float]) -> float:
    sum = 0
    for i in range(0, len(vals) - 1, 1):
        sum += vals[i]
    return sum
