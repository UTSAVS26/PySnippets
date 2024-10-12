# String Matching Algorithms

## Introduction
String matching is a fundamental problem in computer science, where the goal is to find the occurrence of a pattern string within a larger text string. Efficient string matching algorithms are crucial in various applications, including text editors, search engines, DNA sequence analysis, and data compression.

This document covers two popular string matching algorithms: the Naive Approach and the Knuth-Morris-Pratt (KMP) Algorithm.

## Key Concepts

### 1. Naive String Matching Algorithm
The naive string matching algorithm checks for the presence of a pattern in a text by comparing each character of the pattern with each character in the text. It has a straightforward implementation but can be inefficient, particularly for longer strings or patterns.

- **Time Complexity**: O(m * n), where `m` is the length of the pattern and `n` is the length of the text.

### 2. Knuth-Morris-Pratt (KMP) Algorithm
The KMP algorithm improves upon the naive approach by utilizing information gained from previous character comparisons to avoid redundant checks. It preprocesses the pattern to create a "longest prefix suffix" (LPS) array, which helps in determining how many characters can be skipped upon a mismatch.

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

### Knuth-Morris-Pratt (KMP) Algorithm
## Algorithm Steps:

1. Preprocess the pattern to create the LPS array.
2. Iterate through the text and the pattern using the LPS array to skip unnecessary comparisons.
3. If a character mismatch occurs, use the LPS array to determine the next positions to compare.
4. LPS Array Construction:
5. The LPS (Longest Prefix Suffix) array is constructed as follows:

6. LPS[i] represents the longest proper prefix which is also a suffix for the substring pattern[0:i].


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

### Applications of String Matching Algorithms
- Text Search Engines: Finding occurrences of keywords in large texts.
- Data Mining: Searching for patterns in large datasets.
- DNA Sequence Analysis: Searching for patterns in biological sequences.
- Search and Replace Functionality: Implementing find and replace features in text editors.

### Conclusion

Understanding string matching algorithms is essential for efficient text processing and manipulation. The Naive Approach is simple but inefficient for larger datasets, while the KMP algorithm offers a more sophisticated method that significantly improves performance.
