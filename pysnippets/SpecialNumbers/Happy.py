import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def is_happy(number: int) -> bool:
    """
    Determine if a number is a Happy number.

    A Happy number is a number defined by the process of replacing the number by the sum
    of the squares of its digits, repeating the process until the number equals 1 (where it will stay),
    or it loops endlessly in a cycle which does not include 1.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is happy, False otherwise.
    """
    if number < 1:
        logging.error("Number must be a positive integer.")
        raise ValueError("Number must be a positive integer.")

    seen_numbers = set()
    original_number = number

    while number != 1 and number not in seen_numbers:
        seen_numbers.add(number)
        number = sum(int(digit) ** 2 for digit in str(number))
        logging.debug(f"Next number in sequence: {number}")

    if number == 1:
        logging.info(f"{original_number} is a Happy number.")
        return True
    else:
        logging.info(f"{original_number} is not a Happy number.")
        return False

if __name__ == "__main__":
    try:
        is_happy(19)
        is_happy(20)
    except ValueError as ve:
        logging.error(f"Error: {ve}") 