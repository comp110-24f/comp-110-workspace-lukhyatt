"""this program will do something"""

__author__ = "730760282"


def all(int_list: list[int], num: int) -> bool:
    count = 0
    for elem in int_list:
        if elem == num:
            count += 1
    if count == len(int_list) and count != 0:
        return True
    else:
        return False


def max(num_list: list[int]) -> int:
    if len(num_list) == 0:
        raise ValueError("max() arg is an empty list")
    max = num_list[0]
    """over complicated this and tried to make a for loop 
    in a for loop work but this simple for loop that just checks if 
    max > than the the current number works"""
    for elem in num_list:
        if elem > max:
            max = elem
    return max


def is_equal(num_list: list[int], int_list: list[int]) -> bool:
    count = 0
    if len(num_list) == len(int_list):
        for i in range(0, len(num_list)):
            if num_list[i] == int_list[i]:
                count += 1
    if count == len(num_list):
        return True
    return False


def extend(int_list: list[int], num_list: list[int]) -> None:
    for i in range(0, len(num_list)):
        int_list.append(num_list[i])
