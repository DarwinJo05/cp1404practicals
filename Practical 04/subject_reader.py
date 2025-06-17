"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    print(data)
    display_data = display_subject_details(data)
    print(display_data)

def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    subject_data = []
    input_file = open(FILENAME)
    for line in input_file:
        parts = line.split(',')
        parts[2] = int(parts[2])
        subject_data.append(parts)
    input_file.close()
    return subject_data

def display_subject_details(data):
    """Display subject details."""
    for subject in data:
        print(subject[0], "is taught by", subject[1], "and has", subject[2], "students")


main()