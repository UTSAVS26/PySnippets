# Trigonometric Operations Module: trigonometric_operations.py

def radians(degrees):
    """Converts degrees to radians."""
    return degrees * (3.141592653589793 / 180)

def sine(degrees):
    """Returns the sine of the angle in degrees."""
    x = radians(degrees)
    sine_value = 0
    term = x  # First term in the series
    n = 1
    while True:
        sine_value += term
        term *= -x**2 / ((2 * n) * (2 * n + 1))  # Next term in the series
        n += 1
        if abs(term) < 1e-10:  # Stop if the term is very small
            break
    return sine_value

def cosine(degrees):
    """Returns the cosine of the angle in degrees."""
    x = radians(degrees)
    cosine_value = 0
    term = 1  # First term in the series
    n = 0
    while True:
        cosine_value += term
        term *= -x**2 / ((2 * n) * (2 * n - 1))  # Next term in the series
        n += 1
        if abs(term) < 1e-10:  # Stop if the term is very small
            break
    return cosine_value

def tangent(degrees):
    """Returns the tangent of the angle in degrees."""
    return sine(degrees) / cosine(degrees)

# Example usage
if __name__ == "__main__":
    angle = 30
    print("Sine of", angle, "degrees:", sine(angle))
    print("Cosine of", angle, "degrees:", cosine(angle))
    print("Tangent of", angle, "degrees:", tangent(angle))
