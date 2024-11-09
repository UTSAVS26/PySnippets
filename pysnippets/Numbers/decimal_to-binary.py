def decimal_to_binary(decimal_number):
    if isinstance(decimal_number, int):
        return bin(decimal_number)[2:]
    return "Invalid decimal number"

# Example usage
decimal_number = 10
binary_str = decimal_to_binary(decimal_number)
print(f"The binary representation of decimal {decimal_number} is {binary_str}")

# Edge Cases and Limitations:
# - Input: -10 (Negative numbers)
# - Input: "10" (String input)

# Optional Improvements:
# - Add support for floating-point decimal numbers