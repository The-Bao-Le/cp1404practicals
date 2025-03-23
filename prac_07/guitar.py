class Guitar:
    """Represent a guitar entity."""

    def __init__(self, name, year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of guitar entity."""
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def get_age(self):
        """Return the age of the guitar entity."""
        return 2025 - self.year

    def is_vintage(self):
        """Return True if the guitar entity is vintage."""
        return self.get_age() >= 50

