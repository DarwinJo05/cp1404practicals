MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
EXCELLENT = 90
PASSABLE = 50

def main():
    score = -1
    MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"
    print (MENU)
    choice = input("Enter choice: ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_score()
        elif choice == "P":
            score = validate_score(score)
            grade = get_grade(score)
            print(grade)
        elif choice == "S":
            score = validate_score(score)
            stars = display_stars(score)
            print (stars)
        else:
            print("Invalid Choice")
        print(MENU)
        choice = input("Enter choice: ").upper()
    print("Farewell")

def get_score():
    """Get and validate score"""
    score = float(input("Enter score: "))
    while score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        print ("Invalid score")
        score = float(input("Enter score: "))
    return score

def validate_score(score):
    """Validate score"""
    if score <= MINIMUM_SCORE or score >= MAXIMUM_SCORE:
        score = get_score()
        return score

def get_grade(score):
    """Determine grade from the score"""
    if score > EXCELLENT:
        return "Excellent"
    elif score > PASSABLE:
        return "Passable"
    else:
        return "Bad"

def display_stars(score):
    """Print stars"""
    return int(score) * "*"

main()