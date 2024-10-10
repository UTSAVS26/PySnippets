# string_case_conversions.py

def camel_to_snake_case(s:str) -> str:
    """
        Changing the string formatting case from camel case to snake case.

        Example usage:
        camel_to_snake_case("fightForChange") -> "fight_for_change"

    """
    return ''.join(['_' + i.lower() if i.isupper()
                    else i for i in s]).lstrip('_')
def snake_to_camel_case(s:str) -> str:
    """
            Changing the string formatting case from snake case to camel case.

            Example usage:
            camel_to_snake_case("fight_for_change") -> "fightForChange"

    """

    # using for loop to convert string to camel case
    result = ''
    capitalize_next = False
    for char in s:
        if char == '_':
            capitalize_next = True
        else:
            if capitalize_next:
                result += char.upper()
                capitalize_next = False
            else:
                result += char

    return str(result)
# Example usage
if __name__ == '__main__':
    sample_string = "fight_for_change"

    print("Snake case-", sample_string)
    result = snake_to_camel_case(sample_string)
    print('Camelcase-' , result)