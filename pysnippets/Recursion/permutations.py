import logging
from dataclasses import dataclass

logging.basicConfig(level=logging.INFO)

@dataclass
class Permutations:
    string: str

    def generate(self):
        return self._permute(self.string)

    def _permute(self, s, answer=''):
        if len(s) == 0:
            logging.info(f"Permutation: {answer}")
            return [answer]
        results = []
        for i in range(len(s)):
            char = s[i]
            left_substr = s[0:i]
            right_substr = s[i + 1:]
            results += self._permute(left_substr + right_substr, answer + char)
        return results

# Sample usage
if __name__ == "__main__":
    perm = Permutations("abc")
    print(perm.generate())  # Output: All permutations of 'abc' 