import random

MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"

def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_number("Enter score: ", 0, 100)
        elif choice == "P":
            grade = determine_grade(score)
            print(grade)
        elif choice == "S":
            print("*" * score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell.")

def get_valid_number(prompt, low, high):
    """Get valid number from user within range low to high"""
    number = int(input(prompt))
    while number <= low or number >= high:
        print("Invalid input")
        number = int(input(prompt))
    return number

def determine_grade(score):
    """Determine grade based on score"""
    if score >= 90:
        grade = "Excellent"
    elif score >= 50:
        grade = "Passable"
    else:
        grade = "Bad"
    return grade

main()