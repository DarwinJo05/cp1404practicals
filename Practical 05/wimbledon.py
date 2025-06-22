"""
wimbledon
Estimated: 1 hours
Actual:
"""
FILENAME = "wimbledon.csv"

def main():
    data = read_wimbledon_data(FILENAME)
    champion_to_count = count_champions(data)


def read_wimbledon_data(FILENAME):
    """Read file insert into list"""
    with open(FILENAME, "r") as in_file:
        in_file.readline()
        data = [line.strip().split(",") for line in in_file]
    return data

def count_champions(data):
    """Count how many times each champion has won"""
    champion_to_count = {}
    for row in data:
        champion = row[2]
        if champion in champion_to_count:
            champion_to_count[champion] += 1
        else:
            champion_to_count[champion] = 1
    return champion_to_count

main()