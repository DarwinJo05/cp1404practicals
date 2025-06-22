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

def extract_name(email):
    """Extract a name from the email"""
    username = email.split("@")[0]
    parts = username.split('.')
    name = ' '.join(parts).title()
    return name

main()