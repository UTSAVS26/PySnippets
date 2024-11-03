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

if __name__ == "__main__":
    # Example usage
    text = "ababcababcabc"
    pattern = "abc"

    print("Naive String Matching:", naive_string_matching(text, pattern))  # Output: [2, 7, 12]
    print("KMP String Matching:", kmp_string_matching(text, pattern))      # Output: [2, 7, 12]
    print("Boyer-Moore String Matching:", boyer_moore_string_matching(text, pattern))
    print("Finite Automata String Matching:", finite_automata_string_matching(text, pattern))  # Output: [2, 7, 10]
    