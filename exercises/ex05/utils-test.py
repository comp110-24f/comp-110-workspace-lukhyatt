"""this is a place to test utils functions"""

__author__ = "730760282"

from utils import only_evens
from utils import sub
from utils import add_at_index
import pytest


def test_only_evens_u() -> None:
    """use case for [1,2,3]"""
    assert only_evens([1, 2, 3]) == [2]


def test_only_evens_u1() -> None:
    """use case for [1,4,6,3]"""
    assert only_evens([1, 5, 7, 3]) == []


def test_only_evens_e() -> None:
    """edge case for empty list"""
    assert only_evens([]) == []


def test_sub_u() -> None:
    """use case for index 2 to 5 of [1,2,3,4,5]"""
    assert sub([1, 2, 3, 4, 5], 2, 4) == [3, 4]


def test_sub_u1() -> None:
    """use case for index 1 to 4 of [10,25,30,55]"""
    assert sub([10, 25, 30, 55], 1, 4) == [25, 30]


def test_sub2_e() -> None:
    """edge case for if end index is out of bounds"""
    assert sub([10, 25, 30, 55], 1, 7) == [25, 30, 55]


def test_add_at_index_u() -> None:
    """use case for adding 1 at index 3 to [1,2,3,4,5]"""
    use_list = [1, 2, 3, 4, 5]
    add_at_index(use_list, 1, 3)
    assert use_list == [1, 2, 3, 1, 5]


def test_add_at_index_u1() -> None:
    """use case for adding 3 at index 0 to [1,2,3,4,5]"""
    use_list = [1, 2, 3, 4, 5]
    add_at_index(use_list, 3, 0)
    assert use_list == [3, 2, 3, 1, 5]


def test_add_at_index_e() -> None:
    """edge case for if index is out of bounds"""
    with pytest.raises(IndexError):
        add_at_index([1, 2, 3, 4, 5], 1, 7)
