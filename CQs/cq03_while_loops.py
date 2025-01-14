"""this has a function that return that instances of a character in a string"""

__author__ = 730760282


def num_instances(phrase: str, search_char: str) -> int:
    x = 0
    j = 0
    while x < len(phrase):
        if phrase[x] == search_char:
            j += 1
    x += 1
    return j
