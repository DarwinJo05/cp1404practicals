from guitar import Guitar

FILENAME = "guitars.csv"

def main():
    guitars = load_guitars(FILENAME)
    print("These are the guitars loaded:")
    display_guitars(guitars)
    guitars.extend(get_new_guitars())
    guitars.sort()
    print("These are the guitars after adding and sorting:")
    display_guitars(guitars)

    save_guitars(FILENAME, guitars)
    print(f"{len(guitars)} guitars saved to {FILENAME}")

def load_guitars(filename):
    guitars = []
    with open(filename, "r") as in_file:
        for line in in_file:
            parts = line.strip().split(",")
            name = parts[0]
            year = int(parts[1])
            cost = float(parts[2])
            guitars.append(Guitar(name, year, cost))
    return guitars

def display_guitars(guitars):
    for i, guitar in enumerate(guitars, 1):
        print(f"{i}. {guitar}")

def get_new_guitars():
    new_guitars = []
    print("\nEnter new guitars (leave name blank to finish):")
    name = input("Name: ")
    while name != "":
        try:
            year = int(input("Year: "))
            cost = float(input("Cost: "))
            new_guitars.append(Guitar(name, year, cost))
        except ValueError:
            print("Invalid input. Try again.")
        name = input("Name: ")
    return new_guitars

def save_guitars(filename, guitars):
    with open(filename, "w") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)

if __name__ == "__main__":
    main()
