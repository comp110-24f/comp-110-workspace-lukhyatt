from exercises.ex04_utils import is_equal


def test_is_equal() -> None:
    assert is_equal([], []) == False
