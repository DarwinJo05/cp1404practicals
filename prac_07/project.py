class Project:
    """Represent a project with name, start date, priority, cost estimate, and completion percentage."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percent):
        """Initialize a Project instance."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percent = completion_percent

