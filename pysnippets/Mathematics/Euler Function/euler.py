import matplotlib.pyplot as plt
from math import gcd

def euler_totient_function(n):
    """
    Calculate Euler's Totient Function φ(n), which is the count of integers 
    from 1 to n that are coprime with n.
    
    Parameters:
    n (int): Input number
    
    Returns:
    tuple: (Value of φ(n), List of coprime numbers)
    """
    if n <= 0:
        raise ValueError("Input must be a positive integer.")
    
    original_n = n  # Save the original value of n for coprime calculation
    result = n
    coprimes = []

    # Check divisors up to √n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1

    if n > 1:
        result -= result // n

    # Find coprimes using the original n
    for i in range(1, original_n + 1):
        if gcd(i, original_n) == 1:
            coprimes.append(i)

    return result, coprimes

def visualize_coprimes(n, coprimes):
    """
    Visualize coprime numbers up to n using a bar chart.
    
    Parameters:
    n (int): Input number
    coprimes (list): List of coprime numbers
    """
    all_numbers = list(range(1, n + 1))
    coprime_flags = [1 if num in coprimes else 0 for num in all_numbers]

    plt.figure(figsize=(10, 6))
    plt.bar(all_numbers, coprime_flags, color='skyblue', edgecolor='black', label='Coprime')
    plt.title(f"Coprime Numbers Up to {n}", fontsize=16)
    plt.xlabel("Numbers", fontsize=14)
    plt.ylabel("Coprime (1 = Yes, 0 = No)", fontsize=14)
    plt.xticks(range(1, n + 1, max(1, n // 10)))
    plt.yticks([0, 1], labels=["Not Coprime", "Coprime"])
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.legend()
    plt.show()

# Example usage
if __name__ == "__main__":
    num = int(input("Enter a positive integer: "))
    result, coprimes = euler_totient_function(num)
    print(f"φ({num}) = {result}")
    print(f"Coprime numbers up to {num}: {coprimes}")

    visualize_coprimes(num, coprimes)
