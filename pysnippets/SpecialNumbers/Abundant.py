import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def is_abundant(number: int) -> bool:
    """
    Determine if a number is an abundant number.

    An abundant number is a number for which the sum of its proper divisors exceeds the number itself.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is abundant, False otherwise.
    """
    if number < 1:
        logging.error("Number must be a positive integer.")
        raise ValueError("Number must be a positive integer.")

    divisors_sum = sum(i for i in range(1, number) if number % i == 0)
    logging.debug(f"Sum of divisors for {number}: {divisors_sum}")

    if divisors_sum > number:
        logging.info(f"{number} is an Abundant number.")
        return True
    else:
        logging.info(f"{number} is not an Abundant number.")
        return False

if __name__ == "__main__":
    try:
        is_abundant(12)  # Abundant
        is_abundant(28)  # Not Abundant
    except ValueError as ve:
        logging.error(f"Error: {ve}")