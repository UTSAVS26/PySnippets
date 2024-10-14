def is_palindrome(number):
    # Convert the number to a string to easily reverse it
    str_num = str(number)
    
    # Check if the original number is the same as its reverse
    if str_num == str_num[::-1]:
         print(f"{number} is a palindrome.")
    else:
         print(f"{number} is not a palindrome.")


# Example usage
if __name__ == "__main__":
    is_palindrome(101)
    is_palindrome(10)