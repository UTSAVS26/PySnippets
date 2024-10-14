def is_armstrong(number):
    num_str = str(number)
    num_digits = len(num_str)
    
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    if (armstrong_sum == number):
        print(f"{number} is an Armstrong number.")
    else:
        print(f"{number} is not an Armstrong number.")


if __name__ == "__main__":
    # Input from user
    is_armstrong(153)
    is_armstrong(13)
       
