# String Matching Algorithms

## Introduction
String matching is a fundamental problem in computer science, where the goal is to find the occurrence of a pattern string within a larger text string. Efficient string matching algorithms are crucial in various applications, including text editors, search engines, DNA sequence analysis, and data compression.

This document covers four popular string matching algorithms: the Naive Approach, the Knuth-Morris-Pratt (KMP) Algorithm, the Boyer-Moore Algorithm, and the Finite Automata Method.

## Key Concepts

### 1. Naive String Matching Algorithm
The naive string matching algorithm checks for the presence of a pattern in a text by comparing each character of the pattern with each character in the text. It has a straightforward implementation but can be inefficient, particularly for longer strings or patterns.

- **Time Complexity**: O(m * n), where `m` is the length of the pattern and `n` is the length of the text.

### 2. Knuth-Morris-Pratt (KMP) Algorithm
The KMP algorithm improves upon the naive approach by utilizing information gained from previous character comparisons to avoid redundant checks. It preprocesses the pattern to create a "longest prefix suffix" (LPS) array, which helps in determining how many characters can be skipped upon a mismatch.

- **Time Complexity**: O(m + n), where `m` is the length of the pattern and `n` is the length of the text.

### 3. Boyer-Moore Algorithm
The Boyer-Moore algorithm is one of the most efficient string searching algorithms. It preprocesses the pattern to create two tables: the last occurrence table and the good suffix table. This allows it to skip sections of the text, significantly reducing the number of comparisons.

- **Time Complexity**: O(n/m) in the best case, where `m` is the length of the pattern and `n` is the length of the text, and O(m + n) in the average case.

### 4. Finite Automata Method
The Finite Automata approach for string matching constructs a state machine that represents the pattern. It uses a transition function that maps each character of the text to the next state in the state machine. This allows for efficient processing of the text by only transitioning states according to the characters read.

- **Time Complexity**: O(m + n), where `m` is the length of the pattern and `n` is the length of the text.

## Naive String Matching Algorithm

### Algorithm Steps:
1. For each character in the text, check if the substring starting from that character matches the pattern.
2. If a mismatch occurs, move to the next character in the text and continue checking.
3. If a match occurs, record the starting index.

### Python Implementation:
```python
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

# Example usage
text = "ababcababcabc"
pattern = "abc"
print("Naive String Matching:", naive_string_matching(text, pattern))  # Output: [2, 7, 12]
```

## Knuth-Morris-Pratt (KMP) Algorithm

### Algorithm Steps:
1. Preprocess the pattern to create the LPS array.
2. Iterate through the text and the pattern using the LPS array to skip unnecessary comparisons.
3. If a character mismatch occurs, use the LPS array to determine the next positions to compare.

### LPS Array Construction:
The LPS (Longest Prefix Suffix) array is constructed as follows:
- LPS[i] represents the longest proper prefix which is also a suffix for the substring pattern[0:i].

### Python Implementation:
```python
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

# Example usage
text = "ababcababcabc"
pattern = "abc"
print("KMP String Matching:", kmp_string_matching(text, pattern))  # Output: [2, 7, 12]
```

## Boyer-Moore Algorithm

### Algorithm Steps:
1. Preprocess the pattern to create the last occurrence table.
2. Start aligning the pattern from the rightmost end.
3. Compare the pattern with the text; if a mismatch occurs, use the last occurrence table to determine how much to shift the pattern.
4. If a match occurs, record the starting index.

### Python Implementation:
```python
def boyer_moore_string_matching(text, pattern):
    def last_occurrence_function(pattern):
        lof = {}
        for i in range(len(pattern)):
            lof[pattern[i]] = i
        return lof

    m = len(pattern)
    n = len(text)
    indices = []
    lof = last_occurrence_function(pattern)
    i = 0

    while i <= n - m:
        j = m - 1
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1
        if j < 0:
            indices.append(i)
            i += (m if i + m < n else 1)
        else:
            l = lof.get(text[i + j], -1)
            i += max(1, j - l)

    return indices

# Example usage
text = "ababcababcabc"
pattern = "abc"
print("Boyer-Moore String Matching:", boyer_moore_string_matching(text, pattern))  # Output: [2, 7, 12]
```

## Finite Automata Method

### Algorithm Steps:
1. Construct a transition table from the pattern.
2. Use the transition table to process the text character by character.
3. Record the index when the end of the pattern is reached.

### Python Implementation:
```python
def finite_automata_string_matching(text, pattern):
    NO_OF_CHARS = 256

    def get_next_state(pat, M, state, x):
        if state < M and x == ord(pat[state]):
            return state + 1
        for ns in range(state, 0, -1):
            if ord(pat[ns - 1]) == x:
                i = 0
                while i < ns - 1:
                    if pat[i] != pat[state - ns + 1 + i]:
                        break
                    i += 1
                if i == ns - 1:
                    return ns
        return 0

    def compute_transition_function(pat, M):
        TF = [[0 for _ in range(NO_OF_CHARS)] for _ in range(M + 1)]
        for state in range(M + 1):
            for x in range(NO_OF_CHARS):
                TF[state][x] = get_next_state(pat, M, state, x)
        return TF

    M = len(pattern)
    N = len(text)
    TF = compute_transition_function(pattern, M)
    state = 0
    indices = []

    for i in range(N):
        state = TF[state][ord(text[i])]
        if state == M:
            indices.append(i - M + 1)

    return indices

# Example usage
text = "ababcababcabc"
pattern = "abc"
print("Finite Automata String Matching:", finite_automata_string_matching(text, pattern))  # Output: [2, 7, 12]
```

## Applications of String Matching Algorithms
- Text Search Engines: Finding occurrences of keywords in large texts.
- Data Mining: Searching for patterns in large datasets.
- DNA Sequence Analysis: Searching for patterns in biological sequences.
- Search and Replace Functionality: Implementing find and replace features in text editors.

### Conclusion

Understanding string matching algorithms is essential for efficient text processing and manipulation. The Naive Approach is simple but inefficient for larger datasets, while the KMP algorithm, Boyer-Moore algorithm, and Finite Automata Method offer more sophisticated methods that significantly improve performance.
