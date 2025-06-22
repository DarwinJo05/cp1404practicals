"""
Emails
Estimated: 30 minutes
Actual:
"""

def main():
    email_to_name = {}

    email = input("Email: ")
    while email != "":
        name = extract_name(email)
        confirm = input(f"Is your name {name}? (y/n) ").strip().lower()
        if confirm not in ("", "y", "yes"):
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name(email):
    """Extract a name from the email"""
    username = email.split("@")[0]
    parts = username.split('.')
    name = ' '.join(parts).title()
    return name

main()