LENGTH = 10

password = input("Enter password: ")
while len(password) < LENGTH:
    print("Invalid password")
    password = input("Enter password: ")
print(len(password) * '*')