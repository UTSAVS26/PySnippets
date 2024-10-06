# polar_rectangular_conversion.py

import math

def polar_to_rectangular(r, theta):
    """
    Convert polar coordinates to rectangular coordinates.

    Args:
        r (float): The radial distance from the origin.
        theta (float): The angle in radians.

    Returns:
        tuple: The rectangular coordinates as (x, y).

    Example:
        >>> polar_to_rectangular(5, math.pi / 4)
        (3.5355339059327378, 3.5355339059327373)
    """
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return (x, y)

def rectangular_to_polar(x, y):
    """
    Convert rectangular coordinates to polar coordinates.

    Args:
        x (float): The x-coordinate.
        y (float): The y-coordinate.

    Returns:
        tuple: The polar coordinates as (r, theta).

    Example:
        >>> rectangular_to_polar(3, 4)
        (5.0, 0.9272952180016122)
    """
    r = math.sqrt(x ** 2 + y ** 2)
    theta = math.atan2(y, x)
    return (r, theta)

# Example usage
if __name__ == "__main__":
    # Example usage of the functions
    r = 5
    theta = math.pi / 4
    rectangular = polar_to_rectangular(r, theta)
    print("Rectangular Coordinates:", rectangular)

    x, y = 3, 4
    polar = rectangular_to_polar(x, y)
    print("Polar Coordinates:", polar)
