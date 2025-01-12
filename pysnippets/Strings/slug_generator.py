import unicodedata

def generate_slug(text: str) -> str:
    if not isinstance(text, str):
        raise ValueError("Input must be a string.")
    text = text.lower()
    text = "-".join(text.split())

    normalized_text = unicodedata.normalize("NFD", text)
    text = "".join(
        char for char in normalized_text 
        if not unicodedata.combining(char) and (char.isalnum() or char == "-")
    )
    text = text.strip("-")
    text = "-".join([part for part in text.split("-") if part])
    return text

if __name__ == "__main__":
    input_text = "Where to find best cafés in Bhopal?"
    result = generate_slug(input_text)
    print(result)
