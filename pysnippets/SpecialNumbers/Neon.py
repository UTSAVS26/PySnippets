import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def is_neon(number: int) -> bool:
    """
    Determine if a number is a Neon number.

    A Neon number is a number where the sum of the digits of its square is equal to the number itself.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is a Neon number, False otherwise.
    """
    if number < 0:
        logging.error("Number must be a non-negative integer.")
        raise ValueError("Number must be a non-negative integer.")

    square = number ** 2
    digit_sum = sum(int(digit) for digit in str(square))
    logging.debug(f"Digit sum of {square}: {digit_sum}")

    if digit_sum == number:
        logging.info(f"{number} is a Neon number.")
        return True
    else:
        logging.info(f"{number} is not a Neon number.")
        return False

if __name__ == "__main__":
    try:
        is_neon(9)
        is_neon(20)
    except ValueError as ve:
        logging.error(f"Error: {ve}")
       