from dataclasses import dataclass


@dataclass
class Rectangle:
    height: float
    width: float


@dataclass
class Square(Rectangle):
    side: float

    def __post_init__(self):
        super().__init__(self.side, self.side)


@dataclass
class Person:
    name: str
    email: str
    age: int
