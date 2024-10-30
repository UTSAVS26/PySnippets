def is_neon(number):
    square = number ** 2
    digit_sum = sum(int(digit) for digit in str(square))
    if(digit_sum == number):
         print(f"{number} is a Neon number.")
    else:
        print(f"{number} is not a Neon number.")



if __name__ == "__main__":
    is_neon(9)
    is_neon(20)
       