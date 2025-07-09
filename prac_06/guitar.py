CURRENT_YEAR = 2025

class Guitar:
    """Class of Guitar"""

    def __init__(self, name= "", year=0, cost=0):
        """Initialise Guitar with name, year, and cost."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string in the format"""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Return the age of the guitar in years."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Return True if the guitar is 50 or more years old"""
        return self.get_age() >= 50