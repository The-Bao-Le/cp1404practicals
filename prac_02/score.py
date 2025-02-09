"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random
def main():
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))

    grade = determine_grade(score)
    print(grade)

    random_score = random.randint(0, 100)
    random_grade = determine_grade(random_score)
    print(random_grade)

def determine_grade(score):
    if score >= 90:
        grade = "Excellent"
    elif score >= 50:
        grade = "Passable"
    else:
        grade = "Bad"
    return grade

main()