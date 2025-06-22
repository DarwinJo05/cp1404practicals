"""
wimbledon
Estimated: 1 hours
Actual:
"""
FILENAME = "wimbledon.csv"

def main():
    data = read_wimbledon_data(FILENAME)

def read_wimbledon_data(FILENAME):
    with open(FILENAME, "r") as in_file:
        in_file.readline()
        data = [line.strip().split(",") for line in in_file]
    return data

