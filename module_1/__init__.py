from dataclasses import dataclass

from attr import asdict


@dataclass
class InventoryItem:
    """Class for keeping track of an item in inventory."""

    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand


@dataclass
class Point:
    x: int
    y: int

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)


if __name__ == "__main__":
    item = InventoryItem("Super Hoop", 20.0, 2)
    print(item.name)
