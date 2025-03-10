MINIMUM_PASSWORD_LENGTH = 8


def main():
    password = get_password()

    print_password(password)


def print_password(password):
    """Print stars based on password length"""
    print("*" * len(password))


def get_password():
    """Get valid password"""
    password = input("Password: ")
    while len(password) < MINIMUM_PASSWORD_LENGTH:
        print(f"Password must be at least {MINIMUM_PASSWORD_LENGTH} characters long.")
        password = input("Password: ")
    return password


main()