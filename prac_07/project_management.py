import csv
from project import Project
from datetime import datetime

MENU = """
L - Load projects
S - Save projects
D - Display projects
F - Filter projects by date
A - Add new project
U - Update project
Q - Quit"""


def main():
    """Main program to manage projects."""
    FILENAME = "projects.txt"
    projects = load_projects(FILENAME)

    print("Welcome to Pythonic Project Management")
    print(f"Loaded {len(projects)} projects from {FILENAME}")

    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            projects = load_projects(FILENAME)
        elif choice == "S":
            save_projects(FILENAME, projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            date = input("Show projects that start after date (dd/mm/yyyy): ")
            for project in filter_projects_by_date(projects, date):
                print(project)
        elif choice == "A":
            name = input("Name: ")
            start_date = input("Start date (dd/mm/yyyy): ")
            priority = input("Priority: ")
            cost_estimate = float(input(f"Cost estimate: $"))
            completion_percentage = int(input("Percent complete: "))
            projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper()

    if input("Would you like to save to projects.txt? ").lower() == "yes":
        save_projects(FILENAME, projects)
    print("Thank you for using custom-built project management software.")

def load_projects(filename):
    """Load projects from a file."""
    projects = []
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file, delimiter='\t')
            next(reader)
            for row in reader:
                if len(row) == 5:
                    name, start_date, priority, cost_estimate, completion_percentage = row
                    projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))
    except FileNotFoundError:
        print(f"{filename} not found. Starting with an empty list.")
    return projects

def save_projects(filename, projects):
    """Save projects to a file."""
    with open(filename, "w", newline='') as file:
        writer = csv.writer(file, delimiter='\t')
        writer.writerow(["Name", "Start Date", "Priority", "Cost Estimate", "Completion Percentage"])
        for project in projects:
            writer.writerow([project.name, project.start_date.strftime('%d/%m/%Y'),
                             project.priority, project.cost_estimate, project.completion_percentage])

def display_projects(projects):
    """Display incomplete and completed projects."""
    print("Incomplete projects:")
    for project in sorted([p for p in projects if p.completion_percentage < 100], key=lambda x: x.priority):
        print(f"  {project}")
    print("Completed projects:")
    for project in sorted([p for p in projects if p.completion_percentage == 100], key=lambda x: x.priority):
        print(f"  {project}")

def filter_projects_by_date(projects, date):
    """Filter projects that start after the given date."""
    date = datetime.strptime(date, "%d/%m/%Y")
    return [project for project in projects if project.start_date >= date]

def update_project(projects):
    """Allow user to update a project's completion and priority."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    index = int(input("Project choice: "))
    project = projects[index]
    print(project)
    new_percentage = input("New Percentage: ")
    new_priority = input("New Priority: ")
    if new_percentage:
        project.completion_percentage = int(new_percentage)
    if new_priority:
        project.priority = int(new_priority)

if __name__ == "__main__":
    main()