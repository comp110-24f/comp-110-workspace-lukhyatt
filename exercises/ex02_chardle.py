"""EX02- Chardle, a cute step towards wordle"""

__author__ = "730760282"


def input_word() -> str:
    word = str(input("Enter a 5-character word: "))
    if len(word) != 5:
        print("error: word must contain 5 characters.")
        exit()
    print("'" + word + "'")
    return word


def input_letter() -> str:
    letter = str(input("enter a single character: "))
    if len(letter) != 1:
        print("error: Character must be a single character.")
        exit()
    print("'" + letter + "'")
    return letter


def contains_char(word: str, letter: str) -> None:
    j = 0
    i = 0
    print("searching for " + letter + " in " + word)
    while i < (len(word)):
        if word[i] == letter:
            print(letter + " found at index " + str(i))
            j += 1
        i += 1
    if j == 0:
        print("No instances of " + letter + " found in " + word)
    elif j == 1:
        print(str(j) + " instance of " + letter + " found in " + word)
    else:
        print(str(j) + " instances of " + letter + " found in " + word)


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
