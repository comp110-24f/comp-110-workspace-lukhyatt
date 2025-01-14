import math


class circ:

    radius: float

    def __init__(self, r: float):
        self.radius = r

    def get_area(self) -> float:
        return (self.radius**2) * math.pi


class rectangle:

    width: float
    height: float

    def __init__(self, w: float, h: float):
        self.width = w
        self.height = h

    def get_area(self) -> float:
        return self.width * self.height
