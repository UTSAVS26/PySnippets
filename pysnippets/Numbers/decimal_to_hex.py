def decimal_to_hex(decimal_number):
    if isinstance(decimal_number, int):
        return hex(decimal_number)[2:].upper()
    return "Invalid decimal number"

# Example usage
decimal_number = 26
hex_str = decimal_to_hex(decimal_number)
print(f"The hexadecimal representation of decimal {decimal_number} is {hex_str}")

# Edge Cases and Limitations:
# - Input: -26 (Negative numbers)
# - Input: "26" (String input)

# Optional Improvements:
# - Add support for floating-point decimal numbers