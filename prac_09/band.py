class Band:
    """Band class - manages a group of musicians."""

    def __init__(self, name=""):
        """Initialise a Band with a name and empty musician list."""
        self.name = name
        self.musicians = []

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def __str__(self):
        """Return a string representation of the band with its musicians."""
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

    def play(self):
        """Return a string of each musician playing their instrument."""
        return "\n".join(musician.play() for musician in self.musicians)
