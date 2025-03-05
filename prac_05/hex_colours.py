NAME_TO_CODE = {"ABSOLUTE ZERO": "#0048ba", "ACID GREEN": "#b0bf1a", "ALICEBLUE": "#F0F8FF", "AMARANTH": "#e52b50",
                "AMBER": "#ffbf00", "AMETHYST": "#9966cc", "ANTIQUEWHITE": "#FAEBD7", "APRICOT": "#fbceb1",
                "AQUA": "#00ffff", "BLACK": "#000000"}
print(NAME_TO_CODE)

colour_name = input("Enter colour name: ").upper()
while colour_name:
    try:
        print(f"{colour_name} has hex code {NAME_TO_CODE[colour_name]}")
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ").upper()