def hex_to_decimal(hex_str):
    try:
        decimal_number = int(hex_str, 16)
        return decimal_number
    except ValueError:
        return "Invalid hexadecimal number"

# Example usage
hex_str = "1A"
decimal_number = hex_to_decimal(hex_str)
print(f"The decimal representation of hexadecimal {hex_str} is {decimal_number}")

# Edge Cases and Limitations:
# - Input: "G" (Invalid hexadecimal number)
# - Input: "" (Empty string)

# Optional Improvements:
# - Add support for floating-point hexadecimal numbers