"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
EXCELLENT = 90
PASSABLE = 50

def main():
    score = get_score()



def get_score():
    """Get and validate score"""
    score = float(input("Enter score: "))
    while score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        print ("Invalid score")
        score = float(input("Enter score: "))
    return score

else:
    if score > 90:
        print("Excellent")
    elif score > 50:
        print("Passable")
    else:
        print("Bad")