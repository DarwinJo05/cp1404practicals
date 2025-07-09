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