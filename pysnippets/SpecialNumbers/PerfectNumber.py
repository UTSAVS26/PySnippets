import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def is_perfect(number: int) -> bool:
    """
    Determine if a number is a Perfect number.

    A Perfect number is a number that is equal to the sum of its proper divisors.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is perfect, False otherwise.
    """
    if number < 1:
        logging.error("Number must be a positive integer.")
        raise ValueError("Number must be a positive integer.")

    divisors_sum = sum(i for i in range(1, number) if number % i == 0)
    logging.debug(f"Sum of divisors for {number}: {divisors_sum}")

    if divisors_sum == number:
        logging.info(f"{number} is a Perfect number.")
        return True
    else:
        logging.info(f"{number} is not a Perfect number.")
        return False

if __name__ == "__main__":
    try:
        is_perfect(6)
        is_perfect(20)
    except ValueError as ve:
        logging.error(f"Error: {ve}")
       