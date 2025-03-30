import csv
from prac_07.guitar import Guitar


def main():
    """Main program to manage guitars."""
    FILENAME = "guitars.csv"
    guitars = load_guitars(FILENAME)
    guitars.sort()
    display_guitars(guitars)

    name = input("Enter guitar name (or press Enter to quit): ")
    while name:
        year = int(input("Enter year: "))
        cost = float(input("Enter cost: "))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"{new_guitar} added.")
        name = input("Enter guitar name (or press Enter to quit): ")

    guitars.sort()
    save_guitars(FILENAME, guitars)
    print("\nUpdated guitar list:")
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

def save_guitars(filename, guitars):
    """Save guitars to a CSV file."""
    with open(filename, "w", newline='') as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])

def display_guitars(guitars):
    """Display the guitars in a formatted way."""
    print("These are my guitars:")
    for i, guitar in enumerate(guitars, start=1):
        vintage_status = "(Vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar} {vintage_status}")


if __name__ == "__main__":
    main()