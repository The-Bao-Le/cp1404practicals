"""
Emails
Estimate: 30 minutes
Actual:    minutes
"""
def main():
    """Create a dictionary to store email IDs"""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = input("Name: ")
        confirmation = input(f"Is your name {name}? (Y/n) ")
        if confirmation.upper() != "Y" and confirmation != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


main()