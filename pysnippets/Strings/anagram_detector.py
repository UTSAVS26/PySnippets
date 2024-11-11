def are_anagrams(s1: str, s2: str) -> bool:
    if not isinstance(s1, str) or not isinstance(s2, str):
        raise ValueError("Both inputs must be strings.")
    return sorted(s1.replace(" ", "").lower()) == sorted(s2.replace(" ", "").lower())

if __name__ == "__main__":
    string1 = "Listen"
    string2 = "Silent"
    result = are_anagrams(string1, string2)
    print(f"Are '{string1}' and '{string2}' anagrams? {result}")
    # Output: Are 'Listen' and 'Silent' anagrams? True 