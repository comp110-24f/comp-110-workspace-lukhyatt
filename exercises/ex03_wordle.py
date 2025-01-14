"""this program will make wordle"""

__author__ = "730760282"


def input_guess(secret_word_len: int) -> str:
    one = 0
    while one != 1:
        word = input("enter a " + str(secret_word_len) + " character word: ")
        if len(word) == secret_word_len:
            one += 1
        else:
            print("that wasn't " + str(secret_word_len) + " chars!: try again: " + word)
    return word


def contains_char(word: str, letter: str) -> bool:
    """checks if character is in word"""
    assert len(letter) == 1
    i = 0
    while i < len(word):
        if word[i] == letter:
            return True
        i += 1
    return False


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, secret: str) -> str:
    assert len(guess) == len(secret)
    i = 0
    output = ""
    while i < len(secret):
        if secret[i] == guess[i]:
            output += GREEN_BOX
        elif contains_char(secret, guess[i]):
            output += YELLOW_BOX
        else:
            output += WHITE_BOX
        i += 1
    return output


def main(secret: str) -> None:
    """entrypoint of the program and main game loop"""
    turns = 1
    correct = 0
    while turns < 7:
        print("=== Turn " + str(turns) + "/6 ===")
        guess = input_guess(len(secret))
        if guess == secret:
            print(emojified(guess, secret))
            print("you won in " + str(turns) + "/6 turns!")
            turns = 10
            correct = 1
        else:
            print(emojified(guess, secret))
        if turns == 6 and correct == 0:
            print("X/6 - sorry, try again tommorrow")
        turns += 1


if __name__ == "__main__":
    main(secret="codes")
