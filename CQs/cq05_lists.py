"""mutating functions"""

__author__ = "703760282"


def manual_append(num_list: list[int], num: int) -> None:
    num_list.append(num)


def double(dub: list[int]) -> None:
    i = 0
    while i < len(dub):
        dub[i] *= 2
        i += 1


list1: list[int] = [1, 2, 3]

list2: list[int] = list1

double(list2)

print(list1)
print(list2)
