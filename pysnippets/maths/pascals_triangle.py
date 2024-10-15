def pascals_triangle(rows):
    """
    Generate Pascal's Triangle up to a given number of rows.
    
    Args:
        rows (int): The number of rows to generate in Pascal's Triangle.
        
    Returns:
        list of lists: Pascal's Triangle as a list of rows, where each row is a list of integers.
    """
    if rows <= 0:
        raise ValueError("'rows' must be a positive integer.")
    triangle = []
    
    for i in range(rows):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
        
    return triangle

def get_pascals_triangle_row(n):
    """
    Get a specific row from Pascal's Triangle.
    
    Args:
        n (int): The index of the row to retrieve (0-based index).
        
    Returns:
        list: The nth row of Pascal's Triangle.
    """
    if n < 0:
        raise ValueError("n' must be a non-negative integer.")
    row = [1]
    for k in range(1, n + 1):
        row.append(row[-1] * (n - k + 1) // k)
    return row

def binomial_coefficient(n, k):
    """
    Calculate the binomial coefficient (n choose k) using Pascal's Triangle.
    
    Args:
        n (int): The number of items.
        k (int): The number of items to choose.
        
    Returns:
        int: The binomial coefficient.
    """
    if k < 0 or k > n:
        raise ValueError("'k' must be between 0 and 'n' ")
    row = get_pascals_triangle_row(n)
    return row[k]

def print_pascal_triangle(rows):
    """
    Print Pascal's Triangle in a triangular format.
    
    Args:
        rows (int): The number of rows to print.
    """
    triangle = pascals_triangle(rows)
    for row in triangle:
        print(' '.join(map(str, row)).center(2 * rows))
        
def sum_pascals_triangle_row(n):
    """
    Calculate the sum of elements in the nth row of Pascal's Triangle.
    
    Args:
        n (int): The index of the row.
        
    Returns:
        int: The sum of the elements in the nth row.
    """
    return  2 ** n

def factorial(n):
    """
    Calculate the factorial of a number.
    
    Args:
        n (int): The number to calculate the factorial for.
        
    Returns:
        int: The factorial of the number.
    """
    if n < 0:
        raise ValueError("'n' must be non-negative integer.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def polynomial_expansion(a, b, n):
    """
    Expand the binomial expression (a + b)^n using Pascal's Triangle.
    
    Args:
        a (int): The coefficient of the first term.
        b (int): The coefficient of the second term.
        n (int): The power to which the binomial is raised.
        
    Returns:
        str: The expanded form of the binomial expression.
    """
    row = get_pascals_triangle_row(n)
    terms = []
    for k in range(n + 1):
        coefficient = row[k]
        term = f"{coefficient}*{a}^{n - k}*{b}^{k}"
        terms.append(term)
    return ' + '.join(terms)


def pascals_triangle_modulo(rows, mod):
    """
    Generate Pascal's Triangle with elements modulo a given number.
    
    Args:
        rows (int): The number of rows to generate in Pascal's Triangle.
        mod (int): The number for modulo operation.
        
    Returns:
        list of lists: Pascal's Triangle with each element modulo the given number.
    """
    triangle = pascals_triangle(rows)
    return [[element % mod for element in row] for row in triangle]


if __name__ == "__main__":
    rows = 5
    
    triangle = pascals_triangle(rows)
    for row in triangle:
        print(row)
        
    nth_rows = get_pascals_triangle_row(4)
    print(f"4th row of Pascal's Triangle: {nth_rows}")
    
    bin_coeff = binomial_coefficient(5, 2)
    print(f"Binomial coefficient (5 choose 2): {bin_coeff}")
    
    print("Pascal's triangle printed:")
    print_pascal_triangle(5)
    
    sum_row = sum_pascals_triangle_row(4)
    print(f"Sum of elements in the 4th row: {sum_row}")
    
    fact = factorial(5)
    print(f"Factorial of 5: {fact}")
    
    expansion = polynomial_expansion(2, 3, 4)
    print(f"Polynomial expansion of (2 + 3)^4: {expansion}")
    
    mod_triangle = pascals_triangle_modulo(5, 3)
    print(f"Pascal's triangle modulo 3 with 5 rows")
    for row in mod_triangle:
        print(row)
    
    