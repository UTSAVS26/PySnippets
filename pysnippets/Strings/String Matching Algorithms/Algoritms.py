def naive_string_matching(text, pattern):
    m = len(pattern)
    n = len(text)
    indices = []

    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        if j == m:
            indices.append(i)
    
    return indices

def compute_lps(pattern):
    m = len(pattern)
    lps = [0] * m
    length = 0  # Length of the previous longest prefix suffix
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps

def kmp_string_matching(text, pattern):
    n = len(text)
    m = len(pattern)
    lps = compute_lps(pattern)
    indices = []
    i = 0  # Index for text
    j = 0  # Index for pattern

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            indices.append(i - j)
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return indices

if __name__ == "__main__":
    # Example usage
    text = "ababcababcabc"
    pattern = "abc"

    print("Naive String Matching:", naive_string_matching(text, pattern))  # Output: [2, 7, 12]
    print("KMP String Matching:", kmp_string_matching(text, pattern))      # Output: [2, 7, 12]
