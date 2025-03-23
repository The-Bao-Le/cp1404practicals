import csv
from project import Project

MENU = """
Menu:
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
            cost_estimate = float(input("Cost estimate: ").strip("$"))
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