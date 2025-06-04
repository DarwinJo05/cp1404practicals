LENGTH = 10

def main():
    password = validate_password()
    print(len(password) * '*')

def validate_password():
    password = input("Enter password: ")
    while len(password) < LENGTH:
        print("Invalid password")
        password = input("Enter password: ")
    return password
main()