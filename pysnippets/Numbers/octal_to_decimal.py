def octal_to_decimal(octal_str):
    try:
        decimal_number = int(octal_str, 8)
        return decimal_number
    except ValueError:
        return "Invalid octal number"

# Example usage
octal_str = "32"
decimal_number = octal_to_decimal(octal_str)
print(f"The decimal representation of octal {octal_str} is {decimal_number}")

# Edge Cases and Limitations:
# - Input: "8" (Invalid octal number)
# - Input: "" (Empty string)

# Optional Improvements:
# - Add support for floating-point octal numbers