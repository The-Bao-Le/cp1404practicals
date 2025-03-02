FILENAME = "wimbledon.csv"



def main():
    """Read data file and print details about Wimbledon champions and countries."""
    records = load_records(FILENAME)
    champion_to_count, countries = process_records(records)
    display_results(champion_to_count, countries)


def load_records(filename):
    """Load data from a CSV file."""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records
