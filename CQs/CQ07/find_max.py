"""this function will find and thre remove the max value"""

__author__ = "730760282"

def find_and_remove_max(l: list[int])-> int:
    num = 0
    if len(l) == 0:
        return -1
    else:
        for elem in l:
            if elem > num:
                num = elem
        count  = 0
        while count < len(l):
            if l[count] == num:
                l.pop(l[count])
        return num
