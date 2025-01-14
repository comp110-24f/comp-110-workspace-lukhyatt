"""this is a function that uses conditionals to see if you guess a number"""

__author__: str = "730760282"


def guess_a_number() -> None:
    "checks if you guess secret number right"
    secret: int = 7
    x = int(input("Guess a number: "))
    print("Your guess was " + str(x))
    if secret == x:
        print("You got it!")
    elif secret < x:
        print("Your guess was too high! The secret number is " + str(secret))
    elif secret > x:
        print("Your guess was too low! The secret number is " + str(secret))


if __name__ == "__main__":
    guess_a_number()
