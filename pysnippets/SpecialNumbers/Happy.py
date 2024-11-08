def is_happy(number):
    seen = set()
    while number != 1 and number not in seen:
        seen.add(number)
        number = sum(int(digit) ** 2 for digit in str(number))
    if number == 1:
        print(f"{number} is a Happy number.")
    else:
        print(f"{number} is not a Happy number.")

if __name__ == "__main__":
    is_happy(19)
    is_happy(20) 