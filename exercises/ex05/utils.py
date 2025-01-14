"""this is an exercise page about lists"""

__author__ = "730760282"


def only_evens(og_list: list[int]) -> list[int]:
    even_list = []
    # if elem mod 2 == 0 (meaning its even) then we add to list
    for elem in og_list:
        if elem % 2 == 0:
            even_list.append(elem)
    return even_list


def sub(og_list: list[int], start: int, end: int) -> list[int]:
    if start < 0:
        start = 0
    if end > len(og_list):
        end = len(og_list)
    new_list = []
    # adds the values from starting int to ending int to a new list
    for i in range(start, end):
        new_list.append(og_list[i])
    return new_list


def add_at_index(og_list: list[int], new_value: int, idx: int) -> None:
    if idx > len(og_list) or idx < 0:
        raise IndexError("index is out of bounds for the input list")
    if idx == len(og_list):
        og_list.append(new_value)
    # bascially removes numbers in a list and
    # adds them to the end one by one, pauses when we add the new value, then resumes
    else:
        i = 0
        x = 0
        while i < idx:  # removes the numbers before the index
            og_list.append(og_list[x])
            og_list.pop(x)
            i += 1
        og_list.append(new_value)
        x = 0
        i = 0
        while i < ((len(og_list) - idx) - 1):  # removes the numbers after the index
            og_list.append(og_list[x])
            og_list.pop(x)
            i += 1
