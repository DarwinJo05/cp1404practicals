from car import Car
import random

class UnreliableCar(Car):
    """An UnreliableCar that has a chance of not driving."""

    def __init__(self, name, fuel, reliability):
        """Initialise the car with name, fuel and reliability."""
        super().__init__(name, fuel)
        self.reliability = reliability
