"""this is a function that calculates how many teabgs and 
you need for a tea party and the cost"""

__author__: str = "730760282"


def main_planner(guests: int) -> None:
    """the entrypoint of my program"""
    print("A cozy tea party for " + str(guests) + " people!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("cost: $" + str(cost(tea_bags(guests), treats(guests))))


def tea_bags(people: int) -> int:
    """this returns number of teabags needed"""
    return people * 2


def treats(people: int) -> int:
    """this computes number of treats needed"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """computes overall cost needed"""
    return (treat_count * 0.75) + (tea_count * 0.5)


if __name__ == "__main__":
    main_planner(guests=int(input("how many guests are attending your tea party?")))
