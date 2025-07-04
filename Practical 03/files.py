# 1. Write code that asks the user for their name, then opens a file called name.txt and writes that name to it. Use open and close for this question.
FILENAME = "name.txt"
name = input("Enter your name: ")
out_file = open(FILENAME, "w")
out_file.write(name)
out_file.close()

# 2. In the same file, but as if it were a separate program, write code that opens "name.txt" and reads the name (as above) then prints (note the exact output),
# Hi Bob! (or whatever the name is in the file). Do not simply print the user's input variable!
# Use open and close for this question.
FILENAME = "name.txt"
in_file = open(FILENAME, "r")
name = in_file.read()
in_file.close()
print(f"Hi {name}!")

# 3. Write code that opens numbers.txt, reads only the first two numbers, adds them together then prints the result, which should be... 59. Use with instead of open and close for this question.
FILENAME = "numbers.txt"
with open(FILENAME, "r") as in_file:
    first_number = int(in_file.readline())
    second_number = int(in_file.readline())
    total = first_number + second_number
print(total)
in_file.close()

# 4. Now write a fourth block of code that prints the total for all lines in numbers.txt. This should work for a file with any number of numbers. Use with instead of open and close for this question.
FILENAME = "numbers.txt"
with open(FILENAME, "r") as in_file:
    total = 0
    for line in in_file:
        number = int(line)
        total += number
print(total)
in_file.close()
