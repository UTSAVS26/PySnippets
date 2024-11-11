import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def is_deficient(number: int) -> bool:
    """
    Determine if a number is a Deficient number.

    A Deficient number is a number for which the sum of its proper divisors is less than the number itself.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is deficient, False otherwise.
    """
    if number < 1:
        logging.error("Number must be a positive integer.")
        raise ValueError("Number must be a positive integer.")

    divisors_sum = sum(i for i in range(1, number) if number % i == 0)
    logging.debug(f"Sum of divisors for {number}: {divisors_sum}")

    if divisors_sum < number:
        logging.info(f"{number} is a Deficient number.")
        return True
    else:
        logging.info(f"{number} is not a Deficient number.")
        return False

if __name__ == "__main__":
    try:
        is_deficient(15)  # Deficient
        is_deficient(28)  # Not Deficient
    except ValueError as ve:
        logging.error(f"Error: {ve}")