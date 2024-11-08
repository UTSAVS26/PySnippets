import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def is_armstrong(number: int) -> bool:
    """
    Determine if a number is an Armstrong number.

    An Armstrong number is a number that is equal to the sum of its own digits each raised
    to the power of the number of digits.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is an Armstrong number, False otherwise.
    """
    if number < 0:
        logging.error("Number must be a non-negative integer.")
        raise ValueError("Number must be a non-negative integer.")

    num_str = str(number)
    num_digits = len(num_str)
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    logging.debug(f"Armstrong sum for {number}: {armstrong_sum}")

    if armstrong_sum == number:
        logging.info(f"{number} is an Armstrong number.")
        return True
    else:
        logging.info(f"{number} is not an Armstrong number.")
        return False

if __name__ == "__main__":
    try:
        is_armstrong(153)
        is_armstrong(13)
    except ValueError as ve:
        logging.error(f"Error: {ve}")

