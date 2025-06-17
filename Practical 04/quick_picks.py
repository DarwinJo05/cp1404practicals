import random

MIN_NUMBER = 1
MAX_NUMBER = 45

def main():
    number_of_picks = int(input("How many quick picks? "))
    for i in range(number_of_picks):
        quick_pick = generate_quick_pick()
