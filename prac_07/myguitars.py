from guitar import Guitar

FILENAME = "guitars.csv"

def main():
    guitars = load_guitars(FILENAME)
    print("These are the guitars loaded:")
    display_guitars(guitars)
    guitars.extend(get_new_guitars())

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
    print("Enter new guitars :")
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

if __name__ == "__main__":
    main()
