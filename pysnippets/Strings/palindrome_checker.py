import logging
from dataclasses import dataclass

logging.basicConfig(level=logging.INFO)

@dataclass
class PalindromeChecker:
    text: str

    def is_palindrome(self) -> bool:
        sanitized = ''.join(filter(str.isalnum, self.text)).lower()
        return sanitized == sanitized[::-1]

    def longest_palindromic_substring(self) -> str:
        s = ''.join(filter(str.isalnum, self.text)).lower()
        n = len(s)
        if n == 0:
            return ""
        start, end = 0, 0
        for i in range(n):
            len1 = self.expand_from_center(s, i, i)
            len2 = self.expand_from_center(s, i, i + 1)
            max_len = max(len1, len2)
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
        return self.text[start:end + 1]

    @staticmethod
    def expand_from_center(s: str, left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

if __name__ == "__main__":
    checker = PalindromeChecker("A man a plan a canal Panama")
    result = checker.is_palindrome()
    logging.info(f"Is Palindrome: {result}")
    
    longest_palindrome = checker.longest_palindromic_substring()
    logging.info(f"Longest Palindromic Substring: {longest_palindrome}")
    
    checker_empty = PalindromeChecker("")
    result_empty = checker_empty.is_palindrome()
    logging.info(f"Is Palindrome (Empty): {result_empty}")
    
    checker_non_palindrome = PalindromeChecker("OpenAI")
    result_non_palindrome = checker_non_palindrome.is_palindrome()
    logging.info(f"Is Palindrome (OpenAI): {result_non_palindrome}") 