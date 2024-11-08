def is_abundant(number):
    # Calculate the sum of proper divisors
    divisors_sum = sum(i for i in range(1, number) if number % i == 0)
    
    # A number is abundant if the sum of its proper divisors is greater than the number
    if divisors_sum > number:
        print(f"{number} is an Abundant number.")
    else:
        print(f"{number} is not an Abundant number.")

if __name__ == "__main__":
    is_abundant(12)  # Abundant
    is_abundant(28)  # Not Abundant 