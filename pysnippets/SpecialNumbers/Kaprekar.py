import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def is_kaprekar(number: int) -> bool:
    """
    Determine if a number is a Kaprekar number.

    A Kaprekar number is a number whose square can be split into two parts that add up to the original number.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is a Kaprekar number, False otherwise.
    """
    if number < 1:
        logging.error("Number must be a positive integer.")
        raise ValueError("Number must be a positive integer.")

    square = number ** 2
    str_square = str(square)
    length = len(str_square)

    for i in range(1, length):
        left_part = int(str_square[:i])
        right_part = int(str_square[i:])
        logging.debug(f"Splitting {square} into {left_part} and {right_part}")

        if right_part > 0 and (left_part + right_part) == number:
            logging.info(f"{number} is a Kaprekar number.")
            return True

    logging.info(f"{number} is not a Kaprekar number.")
    return False

if __name__ == "__main__":
    try:
        is_kaprekar(297)
        is_kaprekar(10)
    except ValueError as ve:
        logging.error(f"Error: {ve}") 