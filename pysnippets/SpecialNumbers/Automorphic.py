import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def is_automorphic(number: int) -> bool:
    """
    Determine if a number is an Automorphic number.

    An Automorphic number is a number whose square ends with the number itself.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is an Automorphic number, False otherwise.
    """
    if number < 0:
        logging.error("Number must be a non-negative integer.")
        raise ValueError("Number must be a non-negative integer.")

    square = number ** 2
    is_auto = str(square).endswith(str(number))
    logging.debug(f"Square of {number}: {square}")

    if is_auto:
        logging.info(f"{number} is an Automorphic number.")
        return True
    else:
        logging.info(f"{number} is not an Automorphic number.")
        return False

if __name__ == "__main__":
    try:
        is_automorphic(25)
        is_automorphic(16)
    except ValueError as ve:
        logging.error(f"Error: {ve}")