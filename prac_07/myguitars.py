from guitar import Guitar

FILENAME = "guitars.csv"

def main():
    guitars = load_guitars(FILENAME)
    print("These are the guitars loaded:")
    display_guitars(guitars)

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

if __name__ == "__main__":
    main()
