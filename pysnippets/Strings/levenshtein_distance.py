def levenshtein_distance(s1: str, s2: str) -> int:
    if not isinstance(s1, str) or not isinstance(s2, str):
        raise ValueError("Both inputs must be strings.")
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)

    previous_row = list(range(len(s2) + 1))
    for i, c1 in enumerate(s1, 1):
        current_row = [i]
        for j, c2 in enumerate(s2, 1):
            insertions = previous_row[j] + 1
            deletions = current_row[j - 1] + 1
            substitutions = previous_row[j - 1] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    return previous_row[-1]

if __name__ == "__main__":
    string1 = "kitten"
    string2 = "sitting"
    distance = levenshtein_distance(string1, string2)
    print(f"Levenshtein distance between '{string1}' and '{string2}': {distance}")
    # Output: Levenshtein distance between 'kitten' and 'sitting': 3 