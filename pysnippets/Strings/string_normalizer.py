import unicodedata

def normalize_string(s: str) -> str:
    if not isinstance(s, str):
        raise ValueError("Input must be a string.")
    normalized = unicodedata.normalize('NFKD', s)
    return ''.join(c for c in normalized if not unicodedata.combining(c))

if __name__ == "__main__":
    original = "Café Münchner Kindl"
    normalized = normalize_string(original)
    print(normalized)
    # Output: Cafe Munchner Kindl 