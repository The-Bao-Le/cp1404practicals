"""
Pseudocode:
get number_of_gifts, number_of_students
gifts_per_student = number_of_gifts // number_of_students
gifts_left_over = number_of_gifts % number_of_students
display gifts_per_student, gifts_left_over
"""
from itertools import accumulate

# number_of_gifts = int(input("Enter the number of gifts: "))
# number_of_students = int(input("Enter the number of students: "))
# gifts_per_student = number_of_gifts // number_of_students
# gifts_left_over = number_of_gifts % number_of_students
# print("Gifts for each student:", gifts_per_student)
# print("Gifts left over:", gifts_left_over)
"""
GST Calculation
"""
# GST_RATE = 0.09
#
# item_price = float(input("Enter the item price: "))
# tax_status = input("Apply GST (Y/N)? ").upper()
# if tax_status == "Y":
#     item_price *= (1 + GST_RATE)
# print(f"The item price is ${item_price:.2f}")
"""
Loops
"""
# number = int(input("Enter a number: "))
# count = 1
# while count <= number:
#     print(count)
#     count += 1
# print()
# for i in range(1,number + 1):
#     print(i)
"""
Secret number
"""
# import random
# SECRET_NUMBER = random.randint(1, 10)
#
# guess_number = int(input("Guess: "))
# while guess_number != SECRET_NUMBER:
#     print("Wrong number!")
#     guess_number = int(input("Guess: "))
# print("You guessed correctly!")
"""
Input validation
"""
# name = input("Name: ")
# while name == "":
#     print("Name cannot be empty.")
#     name = input("Name: ")
#
# salary = float(input("Salary: "))
# while salary < 0:
#     print("Salary cannot be negative.")
#     salary = float(input("Salary: "))
#
# print(f"Hi {name.upper()}, Your salary is ${salary:.2f}")
"""
Age
"""
# number_of_age = int(input("Number of age: "))
# total_age = 0
# for i in range(number_of_age):
#     age = int(input(f"Age {i+1}: "))
#     total_age += age
# average_age = total_age / number_of_age
# print(f"Total age: {total_age}")
# print(f"Average age: {average_age}")

# age = int(input("Age: "))
# total_age = 0
# count = 0
# while age > 0:
#     total_age += age
#     count += 1
#     age = int(input("Age: "))
# average_age = total_age / count
# print("Total age:", total_age)
# print("Average age:", average_age)
