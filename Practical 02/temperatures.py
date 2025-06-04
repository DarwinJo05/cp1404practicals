def main():
    MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            fahrenheit = convert_celsius_fahrenheit()
            print(f"Result: {fahrenheit:.2f} F")

        elif choice == "F":
            celsius = convert_fahrenheit_celsius()
            print (f"Result: {celsius:.2f} C")

        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

def convert_celsius_fahrenheit():
    """Convert celsius to fahrenheit"""
    celsius = float(input("Celsius: "))
    return celsius * 9.0 / 5 + 32

def convert_fahrenheit_celsius():
    """"Convert fahrenheit to celsius"""
    fahrenheit = float(input("Fahrenheit: "))
    return 5 / 9 * (fahrenheit - 32)

main()