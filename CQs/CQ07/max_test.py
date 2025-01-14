"""file for tests on find_max"""

__author__ = "730760282"

from find_max import find_and_remove_max

def test_max()-> None:
    assert find_and_remove_max([5,6,7,8]) == 8

def test_max_mut()-> None:
    l = [5,6,7,8]
    find_and_remove_max(l)
    assert l == [5,6,7]

def test_max_edge()-> None:
    assert find_and_remove_max([]) == -1
