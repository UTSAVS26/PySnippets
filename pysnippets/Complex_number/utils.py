from complex_number import ComplexNumber
import logging

logger = logging.getLogger(__name__)

def parse_complex(number_str: str) -> ComplexNumber:
    try:
        parts = number_str.replace('i', '').split('+') if '+' in number_str else number_str.replace('i', '').split('-')
        real = float(parts[0].strip())
        imaginary = float(parts[1].strip())
        if '-' in number_str and '+' not in number_str:
            imaginary = -imaginary
        complex_num = ComplexNumber(real, imaginary)
        logger.info(f"Parsed string '{number_str}' into {complex_num}")
        return complex_num
    except Exception as e:
        logger.error(f"Failed to parse '{number_str}': {e}")
        raise ValueError(f"Invalid complex number format: {number_str}") 