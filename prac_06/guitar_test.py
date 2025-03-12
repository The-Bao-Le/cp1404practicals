from prac_06.guitar import Guitar

def main():
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.4)
    another = Guitar("Another Guitar", 2020, 100.4567)
    print(gibson)
    print(another)
    print()
    print(f"Gibson L-5 CES get_age() - Expected 103. Got {gibson.get_age()}")
    print(f"Another Guitar get_age() - Expected 5. Got {another.get_age()}")
    print(f"Gibson L-5 CES is_vintage() - Expected True. Got {gibson.is_vintage()}")
    print(f"Another Guitar is_vintage() - Expected False. Got {another.is_vintage()}")

main()