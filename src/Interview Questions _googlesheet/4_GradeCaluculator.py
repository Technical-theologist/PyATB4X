""""
✅ Grade Calculator:
Write a program that calculates and displays the letter grade for a given numerical score (e.g., A, B, C, D, or F) based on the following grading scale:

A: 90-100
B: 80-89
C: 70-79
D: 60-69
F: 0-59
"""
marks = int(input("Enter the marks: "))
#
# if 90 <= marks <= 100:
#     print("Grade A")
# elif 80 <= marks < 90:
#     print("Grade B")
# elif 70 <= marks < 80:
#     print("Grade C")
# elif 60 <= marks < 70:
#     print("Grade D")
# else:
#     print("Grade F")
#
match marks:
    case marks if 90<=marks<=100:
        print("Grade A")