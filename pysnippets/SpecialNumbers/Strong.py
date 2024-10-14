import math

def is_strong(number):
    num_str = str(number)
    
    # Calculate the sum of factorials of each digit
    strong_sum = sum(math.factorial(int(digit)) for digit in num_str)
    
    # Check if the sum equals the original number
    if (strong_sum == number):
         print(f"{number} is a Strong number.")
    else:
        print(f"{number} is not a Strong number.")


if __name__ == "__main__":
    # Input from user
    is_strong(145)
    is_strong(134)

       
