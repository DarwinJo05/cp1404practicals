COLOUR_NAME_TO_HEX = {
    "aliceBlue": "#f0f8ff",
    "antiqueWhite": "#faebd7",
    "aqua": "#00ffff",
    "aquamarine": "#7fffd4",
    "azure": "#f0ffff",
    "beige": "#f5f5dc",
    "bisque": "#ffe4c4",
    "black": "#000000",
    "blue": "#0000ff",
    "coral": "#FF7F50"
}

colour_name = input("Enter colour: ").lower()
while colour_name != "":
    try:
        print(f"{colour_name.title()} is {COLOUR_NAME_TO_HEX[colour_name]}")
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Enter colour: ").lower()
