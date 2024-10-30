def is_automorphic(number):
    square = number ** 2
    if(str(square).endswith(str(number))):
         print(f"{number} is an Automorphic number.")
    else:
        print(f"{number} is not an Automorphic number.")




if __name__ == "__main__":
   is_automorphic(25)
   is_automorphic(16)