def binary_to_decimal(binary_str):
    try:
        decimal_number = int(binary_str, 2)
        return decimal_number
    except ValueError:
        return "Invalid binary number"

# Example usage
binary_str = "1010"
decimal_number = binary_to_decimal(binary_str)
print(f"The decimal representation of binary {binary_str} is {decimal_number}")

# Edge Cases and Limitations:
# - Input: "2" (Invalid binary number)
# - Input: "" (Empty string)

# Optional Improvements:
# - Add support for floating-point binary numbers