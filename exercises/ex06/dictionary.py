__author__ = "730760282"
"""exercise on dictionaries"""


def invert(og_dict: dict[str, str]) -> dict[str, str]:
    """takes dict and returns an inverted dictionary"""
    # added a raise a keyError if there are duplicate values in the list
    value = ""
    for key in og_dict:
        count = 0
        for x in og_dict:
            if og_dict[key] == og_dict[x]:
                count += 1
            if count >= 2:
                raise KeyError("can't have multiple values in dictionary")
    # iterates through each key and adds the key value pair to new-dict but reversed
    new_dict = {}
    for key in og_dict:
        value = og_dict[key]
        new_dict[value] = key

    return new_dict


def favorite_color(og_dict: dict[str, str]) -> str:
    """returns the most popular color from a dict"""
    x = 0
    color = ""
    # takes an value iterates through each value in dict and increases count each
    # time if the values are equal then checks count against x, our
    # existing highest value
    for elem in og_dict:
        count = 0
        for y in og_dict:
            if og_dict[elem] == og_dict[y]:
                count += 1
        if count > x:
            x = count
            color = og_dict[elem]
    return color


def count(listy: list[str]) -> dict[str, int]:
    """returns a dict with the number of times each key appeared in listy"""
    dicty: dict[str, int] = {}
    # iterates through each element of listy and either adds 1 to an existing key
    # if its a duplicate or makes a new key of value 1
    for elem in listy:
        if elem in dicty:
            dicty[elem] += 1
        else:
            dicty[elem] = 1
    return dicty


def alphabetizer(listy: list[str]) -> dict[str, list[str]]:
    """returns a dict with each first letter that was used the corresponding words that used that letter"""
    dicty: dict[str, list[str]] = {}
    # iterates through each element in listy and adds it to dict corressponding to the right letter
    for elem in listy:
        if elem[0].lower() in dicty:
            dicty[elem[0].lower()].append(elem)
        else:
            dicty[elem[0].lower()] = [elem]
    return dicty


def update_attendance(dicty: dict[str, list[str]], day: str, student: str) -> None:
    """updates the attendance dict based off student name and day they attended"""
    # checks if the day is already in dicty and if it is appends the students name onto the already
    # existing list and if day is not in dict we will add a new key and value
    x = 0
    if day in dicty:
        if student in dicty[day]:
            x = 1
            # honestly I didn't know how to make this if statement just do nothing if student was in
            # dicty so I just made an empty variable because it kept erroring if I didn't put something there
        else:
            dicty[day].append(student)
    else:
        dicty[day] = [student]
