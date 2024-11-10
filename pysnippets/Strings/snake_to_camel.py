def snake_to_camel(snake_str: str) -> str:
    if not isinstance(snake_str, str):
        raise ValueError("Input must be a string.")
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

if __name__ == "__main__":
    snake = "convert_snake_case_to_camelCase"
    camel = snake_to_camel(snake)
    print(camel)
    # Output: convertSnakeCaseToCamelCase 