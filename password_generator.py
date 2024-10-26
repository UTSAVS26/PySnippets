import random
import string

def generate_password(length=12):
    """Generate a random password with letters, digits, and punctuation.

    Args:
        length (int): Length of the password. Defaults to 12.

    Returns:
        str: Generated password.
    """
    if length < 4:  # Ensure there's enough length for variety
        raise ValueError("Password length should be at least 4 characters.")

    # Character pools
    all_chars = string.ascii_letters + string.digits + string.punctuation

    # Randomly generate a password with the specified length
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

if __name__ == "__main__":
    print("Generated password:", generate_password())
