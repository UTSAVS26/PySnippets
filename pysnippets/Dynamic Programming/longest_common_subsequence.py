from dataclasses import dataclass

import logging



@dataclass

class LCSInput:

    x: str

    y: str



def longest_common_subsequence(input_data: LCSInput):

    try:

        x, y = input_data.x, input_data.y

        m, n = len(x), len(y)

        dp = [[0] * (n + 1) for _ in range(m + 1)]



        for i in range(1, m + 1):

            for j in range(1, n + 1):

                if x[i - 1] == y[j - 1]:

                    dp[i][j] = dp[i - 1][j - 1] + 1

                else:

                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])



        return dp[m][n]

    except Exception as e:

        logging.error(f"Error calculating LCS: {e}")

        return None



# Test cases

def test_longest_common_subsequence():

    test_cases = [

        (LCSInput("AGGTAB", "GXTXAYB"), 4),

        (LCSInput("ABCBDAB", "BDCAB"), 4),

        (LCSInput("", ""), 0),

        (LCSInput("ABC", "AC"), 2),

    ]

    

    for input_data, expected in test_cases:

        result = longest_common_subsequence(input_data)

        assert result == expected, f"Expected {expected}, got {result}"



if __name__ == "__main__":

    test_longest_common_subsequence()
