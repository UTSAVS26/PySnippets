from dataclasses import dataclass

import logging



@dataclass

class EditDistanceInput:

    s1: str

    s2: str



def edit_distance(input_data: EditDistanceInput):

    try:

        s1, s2 = input_data.s1, input_data.s2

        m, n = len(s1), len(s2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]



        for i in range(m + 1):

            for j in range(n + 1):

                if i == 0:

                    dp[i][j] = j

                elif j == 0:

                    dp[i][j] = i

                elif s1[i - 1] == s2[j - 1]:

                    dp[i][j] = dp[i - 1][j - 1]

                else:

                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])



        return dp[m][n]

    except Exception as e:

        logging.error(f"Error calculating edit distance: {e}")

        return None



# Test cases

def test_edit_distance():

    test_cases = [

        (EditDistanceInput("horse", "ros"), 3),

        (EditDistanceInput("intention", "execution"), 5),

        (EditDistanceInput("", ""), 0),

        (EditDistanceInput("a", "b"), 1),

        (EditDistanceInput("abc", "yabd"), 2),

    ]

    

    for input_data, expected in test_cases:

        result = edit_distance(input_data)

        assert result == expected, f"Expected {expected}, got {result}"



if __name__ == "__main__":

    test_edit_distance()


