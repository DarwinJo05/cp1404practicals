"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
EXCELLENT = 90
PASSABLE = 50
import random

def main():
    score = get_score()
    grade = get_grade(score)
    print(grade)
    random_number = random.randint(MINIMUM_SCORE, MAXIMUM_SCORE)
    random_grade = get_grade(random_number)
    print(random_grade)

def get_score():
    """Get and validate score"""
    score = float(input("Enter score: "))
    while score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        print ("Invalid score")
        score = float(input("Enter score: "))
    return score

def get_grade(score):
    """Determine grade from the score"""
    if score > EXCELLENT:
        return "Excellent"
    elif score > PASSABLE:
        return "Passable"
    else:
        return "Bad"

main()