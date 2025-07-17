from project import Project

FILENAME = "projects.txt"

def main():
    """Load projects from file and display them."""
    projects = load_projects(FILENAME)
    print("Projects loaded from file:")
    for project in projects:
        print(project)

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

if __name__ == "__main__":
    main()
