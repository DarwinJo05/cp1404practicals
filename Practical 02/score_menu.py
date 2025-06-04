MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100

def main():
    MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"
    print (MENU)
    choice = input("Enter hoice: ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_score()


def get_score():
    """Get and validate score"""
    score = float(input("Enter score: "))
    while score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        print ("Invalid score")
        score = float(input("Enter score: "))
    return score

main()