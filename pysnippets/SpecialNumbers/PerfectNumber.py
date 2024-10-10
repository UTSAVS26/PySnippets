def is_perfect(number):
    # Find all divisors of the number (excluding the number itself)
    divisors_sum = sum(i for i in range(1, number) if number % i == 0)
    
    # Check if the sum of divisors equals the original number
    if (divisors_sum == number):
         print(f"{number} is a Perfect number.")
    else:
        print(f"{number} is not a Perfect number.")



if __name__ == "__main__":
    # Input from user
    is_perfect(6)
    is_perfect(20)
       