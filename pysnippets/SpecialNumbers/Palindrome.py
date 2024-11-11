import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def is_palindrome(number: int) -> bool:
    """
    Determine if a number is a palindrome.

    A palindrome number is a number that remains the same when its digits are reversed.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is a palindrome, False otherwise.
    """
    if number < 0:
        logging.error("Number must be a non-negative integer.")
        raise ValueError("Number must be a non-negative integer.")

    str_num = str(number)
    is_palin = str_num == str_num[::-1]
    logging.debug(f"Original number: {str_num}, Reversed: {str_num[::-1]}")

    if is_palin:
        logging.info(f"{number} is a palindrome.")
        return True
    else:
        logging.info(f"{number} is not a palindrome.")
        return False

if __name__ == "__main__":
    try:
        is_palindrome(101)
        is_palindrome(10)
    except ValueError as ve:
        logging.error(f"Error: {ve}")