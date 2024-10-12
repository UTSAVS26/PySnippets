import math

def polar_to_rectangular(r, theta, degrees=False):
    """
    Convert polar coordinates to rectangular coordinates.

    Args:
        r (float): The radial distance from the origin.
        theta (float): The angle in radians or degrees.

    Returns:
        tuple: The rectangular coordinates as (x, y).

    Example:
        >>> polar_to_rectangular(5, math.pi / 4)
        (3.5355339059327378, 3.5355339059327373)
    """
    if degrees:
        theta = math.radians(theta)
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return (x, y)

def rectangular_to_polar(x, y, degrees=False):
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
    if degrees:
        theta = math.degrees(theta)
    return (r, theta)

def bulk_polar_to_rectangular(polar_list, degrees=False):
    """
    Convert a list of polar coordinates to rectangular coordinates.

    Args:
        polar_list (list): List of tuples containing polar coordinates (r, theta).
        degrees (bool): Whether the angles are in degrees.

    Returns:
        list: List of rectangular coordinates.
    """
    return [polar_to_rectangular(r, theta, degrees) for r, theta in polar_list]

def bulk_rectangular_to_polar(rectangular_list, degrees=False):
    """
    Convert a list of rectangular coordinates to polar coordinates.

    Args:
        rectangular_list (list): List of tuples containing rectangular coordinates (x, y).
        degrees (bool): Whether to return the angle in degrees.

    Returns:
        list: List of polar coordinates.
    """
    return [rectangular_to_polar(x, y, degrees) for x, y in rectangular_list]

def cylindrical_to_rectangular(r, theta, z, degrees=False):
    """
    Convert cylindrical coordinates to rectangular coordinates.

    Args:
        r (float): The radial distance.
        theta (float): The angle in radians or degrees.
        z (float): The height along the z-axis.
        degrees (bool): Whether theta is in degrees. Defaults to False.

    Returns:
        tuple: The rectangular coordinates as (x, y, z).
    """
    if degrees:
        theta = math.radians(theta)
    
    x, y = polar_to_rectangular(r, theta)
    return (x, y, z)

def rectangular_to_cylindrical(x, y, z, degrees=False):
    """
    Convert rectangular coordinates to cylindrical coordinates.

    Args:
        x (float): X-coordinate.
        y (float): Y-coordinate.
        z (float): Height along the z-axis.

    Returns:
        tuple: Cylindrical coordinates as (r, theta, z).
    """
    r, theta = rectangular_to_polar(x, y, degrees)
    return (r, theta, z)

def polar_to_complex(r, theta, degrees=False):
    """
    Convert polar coordinates to a complex number.

    Args:
        r (float): Radial distance.
        theta (float): Angle in radians (or degrees if specified).

    Returns:
        complex: Complex number.
    """
    if degrees:
        theta = math.radians(theta)
    return complex(r * math.cos(theta), r * math.sin(theta))

def complex_to_polar(c, degrees=False):
    """
    Convert a complex number to polar coordinates.

    Args:
        c (complex): A complex number.

    Returns:
        tuple: Polar coordinates as (r, theta).
    """
    r = abs(c)
    theta = math.atan2(c.imag, c.real)
    if degrees:
        theta = math.degrees(theta)
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
