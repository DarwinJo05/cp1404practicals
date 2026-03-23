from car import Car
import random

class UnreliableCar(Car):
    """An UnreliableCar that has a chance of not driving."""

    def __init__(self, name, fuel, reliability):
        """Initialise the car with name, fuel and reliability."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Attempt to drive the car based on reliability.
        Drive only if a random number is less than reliability.
        """
        if random.uniform(0, 100) < self.reliability:
            return super().drive(distance)
        else:
            return 0