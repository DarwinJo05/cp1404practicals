from project import Project

FILENAME = "projects.txt"

def main():
    """Display menu and manage project options."""
    projects = load_projects(FILENAME)
    print("Projects loaded from file.")

    MENU = "\n(L)oad projects\n(S)ave projects\n(D)isplay projects\n(F)ilter projects by date\n(A)dd new project\n(U)pdate project\n(Q)uit"
    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "D":
            display_projects(projects)
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
    for project in projects:
        print(project)

if __name__ == "__main__":
    main()
