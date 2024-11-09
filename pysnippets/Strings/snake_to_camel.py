def snake_to_camel(snake_str: str) -> str:
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

if __name__ == "__main__":
    snake = "convert_snake_case_to_camelCase"
    camel = snake_to_camel(snake)
    print(camel)
    # Output: convertSnakeCaseToCamelCase 