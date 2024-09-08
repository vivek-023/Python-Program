import re

def is_valid_email(email):
    """Validate the email address using a regular expression."""
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email)

def email_slicer(email):
    """Slice the email address into username and domain."""
    try:
        username, domain = email.split('@')
        return username, domain
    except ValueError:
        return None, None

def main():
    """Main function to run the email slicer."""
    while True:
        # Prompt the user for input
        email = input("Please enter your email address (or type 'exit' to quit): ")
        
        # Check if the user wants to exit the program
        if email.lower() == 'exit':
            print("Goodbye!")
            break

        # Validate the email address
        if is_valid_email(email):
            # Slice the email into username and domain
            username, domain = email_slicer(email)
            if username and domain:
                print(f"Username: {username}")
                print(f"Domain: {domain}")
            else:
                print("Error: Could not slice the email address correctly.")
        else:
            print("Invalid email address. Please try again.")

if __name__ == "__main__":
    main()
