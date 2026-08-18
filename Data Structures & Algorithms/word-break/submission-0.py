class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        # Key Data Structure: Dynamic Programming (Bottom-Up)

        dp = [False] * (len(s) + 1)  # dp[i] = can s[i:] be fully segmented into dictionary words?
        dp[len(s)] = True  # base case: empty remaining string is trivially "breakable"

        # walk backwards from the end of the string to the start
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                # check if word w fits starting at position i, and matches exactly
                if (i + len(w)) <= len(s) and s[i:i + len(w)] == w:
                    # if w matches here, whether s[i:] is breakable depends on
                    # whether the REST of the string (after this word) is breakable
                    dp[i] = dp[i + len(w)]

                if dp[i]:
                    break  # found a word that works — no need to try other words at this position

        return dp[0]  # can the entire string s (starting at index 0) be segmented?

        # Time Complexity:  O(n * m * k) — n=len(s), m=number of words, k=avg word length (for slicing/comparison)
        # Space Complexity: O(n) — dp array of size n+1