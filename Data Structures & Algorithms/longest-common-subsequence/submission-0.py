class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        # Key Data Structure: Dynamic Programming (Bottom-Up, 2D Grid)

        m, n = len(text1), len(text2)

        # dp[i][j] = LCS length using the first i chars of text1 and first j chars of text2
        # extra row/col of 0s handles the "empty string" base case
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # build forward, filling in each cell using previously computed cells
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # note: i-1 and j-1 because dp is offset by 1 (dp[1][1] represents
                # the first character of each string, i.e. text1[0] and text2[0])
                if text1[i - 1] == text2[j - 1]:
                    # characters match — extend the LCS found without these two characters
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    # no match — take the best result from skipping a char in either string
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[m][n]  # LCS length using the FULL length of both strings

        # Time Complexity:  O(m*n) — fill every cell of the grid once
        # Space Complexity: O(m*n) — full 2D table (could be optimized to O(min(m,n)))

        # Top-Down DP (Memoization) — alternate approach, kept as reference below
        # m, n = len(text1), len(text2)
        # memo = {}
        #
        # def longest(i, j):
        #     if (i, j) in memo:
        #         return memo[(i, j)]  # already computed, return cached result
        #
        #     if i == m or j == n:
        #         return 0  # ran out of characters in one string
        #
        #     if text1[i] == text2[j]:
        #         result = 1 + longest(i + 1, j + 1)  # match — count it, advance both
        #     else:
        #         result = max(longest(i, j + 1), longest(i + 1, j))  # skip one char, try both ways
        #
        #     memo[(i, j)] = result
        #     return result
        #
        # return longest(0, 0)