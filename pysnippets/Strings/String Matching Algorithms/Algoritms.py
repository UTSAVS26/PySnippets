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

def rabin_karp(text,pattern,q):
    '''this algorithm uses a rolling hash function which generates hash value for text and pattern
    and it matches all the text hash value with the pattern value and checks the string only when the hash is same'''
    
    #d is the number of characters in the input alphabet
    d = 256
    n = len(text)
    m = len(pattern)
    i = 0  #index for text
    j = 0  #index for pattern
    hashp = 0 #hash value for pattern
    hasht = 0 #hash value for text
    h = 1
    indices = []
    #the value of h would be "pow(d,m-1)%q"
    for i in range(m-1):
        h = (h*d)%q

    '''Calculate the hash value of pattern and first window of text'''
    for i in range(m):
        hashp = (d*hashp + ord(pattern[i]))%q
        hasht = (d*hasht + ord(text[i]))%q

    for i in range(n-m+1):
        if hashp==hasht:
            for j in range(m):
                if text[i+j] != pattern[j]:
                    break
                else:
                    j += 1

            if j == m:
                indices.append(i)
        
        if i<n-m:
            hasht = (d*(hasht-ord(text[i])*h)+ord(text[i+m]))%q
            if hasht<0:
                hasht = hasht + q

    return indices

def BadCharHeuristic(string,size):
    '''
    the preprocessing function for boyer moore's bad character heuristic
    '''
    no_of_char = 256
    badChar = [-1]*no_of_char #initialising all occirencs as -1

    for i in range(size):
        badChar[ord(string[i])] = i

    return badChar

def Boyer_Moore(pattern,text):
    '''
    A pattern searching function that uses Bad Character
    Heuristic of Boyer Moore Algorithm
    '''
    m = len(pattern)
    n = len(text)
    #creating bad character list
    badChar = BadCharHeuristic(pattern,m)
    indices = []
    s = 0
    while(s <= n-m):
        j = m-1 
        while j>=0 and pattern[j] == text[s+j]:
           j -= 1

        if j<0:
            indices.append(s)
            s += (m-badChar[ord(text[s+m])] if s+m < n else 1)
        else:
            s += max(1,j-badChar[ord(text[s+j])])  
    
    return indices


if __name__ == "__main__":
    # Example usage
    text = "ababcababcabc"
    pattern = "abc"

    q = 101 # a prime number
    print("Naive String Matching:", naive_string_matching(text, pattern))  # Output: [2, 7, 12]
    print("KMP String Matching:", kmp_string_matching(text, pattern))      # Output: [2, 7, 12]
    print("rabin karp algorithm:", rabin_karp(text,pattern,q))
    print("boyer moore string matching using bad heuristic: ", Boyer_Moore(pattern,text))
