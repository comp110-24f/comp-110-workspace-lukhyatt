def check_first_letter(word: str, letter: str) -> str:
    if letter == word[0]:
        return "match!"
    else:
        return "no match!"


check_first_letter("hello", "h")


def lessen(my_list: list[int]):
    idx: int = 0
    while idx < len(my_list):
        my_list[idx] = my_list[idx] - 1
        idx += 1
    return my_list


msg: list[int] = [4, 5, 6]
print(lessen(msg))
