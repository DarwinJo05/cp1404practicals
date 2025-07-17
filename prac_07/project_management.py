from datetime import datetime
from project import Project

FILENAME = "projects.txt"
MENU = "\n(L)oad projects\n(S)ave projects\n(D)isplay projects\n(F)ilter projects by date\n(A)dd new project\n(U)pdate project\n(Q)uit"

def main():
    """Display menu and manage project options."""
    projects = load_projects(FILENAME)
    print("Projects loaded from file.")

    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "L":
            filename = input("Filename to load projects from: ")
            projects = load_projects(filename)
            print(f"Projects loaded from {filename}")

        elif choice == "S":
            filename = input("Filename to save projects to: ")
            save_projects(filename, projects)

        if choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects_by_date(projects)
        elif choice == "A":
            add_new_project(projects)
        elif choice == "U":
            update_project(projects)

        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()

    print("Goodbye")

def load_projects(filename):
    """Read projects and return a list of Project objects."""
    projects = []
    with open(filename, "r") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split('\t')
            name = parts[0]
            start_date = parts[1]
            priority = int(parts[2])
            cost_estimate = float(parts[3])
            completion_percent = int(parts[4])
            project = Project(name, start_date, priority, cost_estimate, completion_percent)
            projects.append(project)
    return projects

def display_projects(projects):
    """Display all loaded projects."""
    incomplete = [p for p in projects if p.completion_percent < 100]
    complete = [p for p in projects if p.completion_percent == 100]

    print("Incomplete projects:")
    incomplete_sorted = sort_projects_by_priority(incomplete)
    for project in incomplete_sorted:
        print(f"  {project}")

    print("Completed projects:")
    complete_sorted = sort_projects_by_priority(complete)
    for project in complete_sorted:
        print(f"  {project}")

def filter_projects_by_date(projects):
    """Filter and display projects that start after a given date."""
    date_input = input("Show projects that start after date (dd/mm/yyyy): ")
    try:
        filter_date = datetime.strptime(date_input, "%d/%m/%Y").date()
    except ValueError:
        print("Invalid date format")
        return

    filtered_projects = []
    for p in projects:
        project_date = datetime.strptime(p.start_date, "%d/%m/%Y").date()
        if project_date > filter_date:
            filtered_projects.append(p)

    filtered_sorted = sort_projects_by_start_date(filtered_projects)
    for project in filtered_sorted:
        print(project)

def add_new_project(projects):
    """Add a new project to the list."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percent = int(input("Percent complete: "))

    project = Project(name, start_date, priority, cost_estimate, completion_percent)
    projects.append(project)
    print(f"Project '{name}' added.")

def update_project(projects):
    """Update an existing project's completion percentage and/or priority."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    try:
        choice = int(input("Project choice: "))
        project = projects[choice]
    except (ValueError, IndexError):
        print("Invalid project choice")
        return

    print(project)
    new_percent = input("New Percentage: ")
    if new_percent:
        project.completion_percent = int(new_percent)

    new_priority = input("New Priority: ")
    if new_priority:
        project.priority = int(new_priority)

def sort_projects_by_priority(projects):
    """Return a list of projects sorted by priority."""
    return sorted(projects, key=get_priority)

def sort_projects_by_start_date(projects):
    """Return a list of projects sorted by start date."""
    return sorted(projects, key=get_start_date)

def get_priority(project):
    return project.priority

def get_start_date(project):
    return datetime.strptime(project.start_date, "%d/%m/%Y")

def save_projects(filename, projects):
    """Save list of projects to the given filename."""
    with open(filename, 'w') as out_file:
        out_file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percent\n")
        for project in projects:
            out_file.write(f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percent}\n")
    print(f"Projects saved to {filename}")

if __name__ == "__main__":
    main()
