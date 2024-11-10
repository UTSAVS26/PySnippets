class ComplexNumberError(Exception):
    """Base exception class for ComplexNumber operations."""
    pass

class DivisionByZeroError(ComplexNumberError):
    """Exception raised when attempting to divide by zero."""
    pass 