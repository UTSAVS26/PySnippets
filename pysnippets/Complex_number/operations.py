from complex_number import ComplexNumber
from logger_config import setup_logger

logger = setup_logger(__name__)

def power(complex_num: ComplexNumber, exponent: int) -> ComplexNumber:
    if exponent == 0:
        logger.info(f"Power: {complex_num} ** {exponent} = 1 + 0i")
        return ComplexNumber(1, 0)
    if exponent < 0:
        logger.error("Negative exponents are not supported.")
        raise ValueError("Negative exponents are not supported.")
    try:
        result = ComplexNumber(1, 0)  # Initialize result as 1 + 0i
        for _ in range(exponent):
            result = result.multiply(complex_num)
        logger.info(f"Power: {complex_num} ** {exponent} = {result}")
        return result
    except Exception as e:
        logger.error(f"Error computing power: {e}")
        raise ValueError("Invalid exponent value.") 