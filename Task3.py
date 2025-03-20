import random
import string

def generate_password(length):
    """Generate a strong random password of specified length."""
    if length < 4:
        print("Password length should be at least 4 for security!")
        return None

    # Define character sets
    lower = string.ascii_lowercase  # a-z
    upper = string.ascii_uppercase  # A-Z
    digits = string.digits          # 0-9
    special = string.punctuation    # Special characters like !@#$%^&*

    # Ensure at least one of each type is included
    all_chars = lower + upper + digits + special
    password = (
        random.choice(lower) +
        random.choice(upper) +
        random.choice(digits) +
        random.choice(special) +
        ''.join(random.choice(all_chars) for _ in range(length - 4))
    )

    # Shuffle the password to mix characters
    password = ''.join(random.sample(password, len(password)))
    return password

# Get user input for password length
try:
    length = int(input("Enter the desired password length: "))
    password = generate_password(length)
    if password:
        print(f"Generated Password: {password}")
except ValueError:
    print("Invalid input! Please enter a valid number.")
