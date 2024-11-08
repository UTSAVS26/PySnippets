import logging
import math

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def is_strong(number: int) -> bool:
    """
    Determine if a number is a Strong number.

    A Strong number is a number in which the sum of the factorial of its digits is equal
    to the number itself.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is a Strong number, False otherwise.
    """
    if number < 0:
        logging.error("Number must be a non-negative integer.")
        raise ValueError("Number must be a non-negative integer.")

    num_str = str(number)
    strong_sum = sum(math.factorial(int(digit)) for digit in num_str)
    logging.debug(f"Sum of factorials for {number}: {strong_sum}")

    if strong_sum == number:
        logging.info(f"{number} is a Strong number.")
        return True
    else:
        logging.info(f"{number} is not a Strong number.")
        return False

if __name__ == "__main__":
    try:
        is_strong(145)
        is_strong(134)
    except ValueError as ve:
        logging.error(f"Error: {ve}")

       
