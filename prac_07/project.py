class Project:
    """Represent a project entity."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialize a Project instance."""
        self.name = name
        self.start_date = start_date
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __str__(self):
        """Return a string representation of the project."""
        return (f"{self.name}, Start Date: {self.start_date}, "
                f"Priority: {self.priority}, Cost Estimate: ${self.cost_estimate:.2f}, "
                f"Completion: {self.completion_percentage}%")

    def __lt__(self, other):
        """Compare projects based on start date."""
        return self.start_date < other.start_date