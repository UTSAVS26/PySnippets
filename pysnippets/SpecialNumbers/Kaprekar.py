def is_kaprekar(number):
    square = number ** 2
    str_sq = str(square)
    for i in range(1, len(str_sq)):
        left = int(str_sq[:i])
        right = int(str_sq[i:])
        if right > 0 and left + right == number:
            print(f"{number} is a Kaprekar number.")
            return
    print(f"{number} is not a Kaprekar number.")

if __name__ == "__main__":
    is_kaprekar(297)
    is_kaprekar(10) 