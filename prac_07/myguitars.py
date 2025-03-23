import csv
from prac_07.guitar import Guitar

def main():
    """Main program to manage guitars."""
    FILENAME = "guitars.csv"
    guitars = load_guitars(FILENAME)
    display_guitars(guitars)


def load_guitars(filename):
    """Load guitars from a CSV file."""
    guitars = []
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 3:
                    name, year, cost = row[0], int(row[1]), float(row[2])
                    guitars.append(Guitar(name, year, cost))
    except FileNotFoundError:
        print(f"{filename} not found. Starting with an empty list.")
    return guitars


def display_guitars(guitars):
    """Display the guitars in a formatted way."""
    print("These are my guitars:")
    for i, guitar in enumerate(guitars, start=1):
        vintage_status = "(Vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar} {vintage_status}")


if __name__ == "__main__":
    main()