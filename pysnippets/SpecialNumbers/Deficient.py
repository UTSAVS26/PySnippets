def is_deficient(number):
    # Calculate the sum of proper divisors
    divisors_sum = sum(i for i in range(1, number) if number % i == 0)
    
    # A number is deficient if the sum of its proper divisors is less than the number
    if divisors_sum < number:
        print(f"{number} is a Deficient number.")
    else:
        print(f"{number} is not a Deficient number.")

if __name__ == "__main__":
    is_deficient(15)  # Deficient
    is_deficient(28)  # Not Deficient 