import random

MIN_NUMBER = 1
MAX_NUMBER = 45

def main():
    number_of_picks = int(input("How many quick picks? "))
    for i in range(number_of_picks):
        quick_pick = generate_quick_pick()
        print(" ".join(f"{number:2}" for number in quick_pick))

def generate_quick_pick():
    """Generate six random numbers and put them in a list."""
    numbers = []
    while len(numbers) < 6:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in numbers:
            numbers.append(number)
    numbers.sort()
    return numbers

main()