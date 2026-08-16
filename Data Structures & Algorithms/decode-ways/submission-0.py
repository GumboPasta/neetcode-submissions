class Solution:
    def numDecodings(self, s: str) -> int:

        # Key Data Structure: Dynamic Programming (Bottom-Up)

        dp = {len(s): 1}  # base case: empty remaining string = 1 way (the "do nothing" decode)

        # walk backwards from the end of the string to the start
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0   # '0' can never start a valid single-digit decode, dead end
            else:
                dp[i] = dp[i + 1]   # decode s[i] alone as one digit, carry forward ways from i+1

            # check if s[i:i+2] forms a valid two-digit decode (10-26)
            if (i + 1 < len(s) and (s[i] == "1" or
                s[i] == "2" and s[i + 1] in "0123456")):
                dp[i] += dp[i + 2]   # add ways from decoding two digits together

        return dp[0]  # total ways to decode the entire string

        # Time Complexity:  O(n) — single pass through the string
        # Space Complexity: O(n) — dp dictionary stores one entry per index

        # ⚠️ NOTE: code below this point is unreachable — the function already
        # returned above. Kept here only as reference for the alternate top-down approach.

        # Top-Down DP (Memoization) version:
        # dp = {len(s): 1}

        # def dfs(i):
        #     if i in dp:
        #         return dp[i]   # already computed, return cached result
        #     if s[i] == "0":
        #         return 0        # '0' can't start a valid decode

        #     res = dfs(i + 1)    # decode s[i] as a single digit, recurse on the rest

        #     # check if the two-digit combo s[i:i+2] is valid (10-26)
        #     if (i + 1 < len(s) and (s[i] == "1" or
        #         s[i] == "2" and s[i + 1] in "0123456")):
        #         res += dfs(i + 2)   # ⚠️ BUG: this was written as dfs[i+2] (subscript)
        #                              # should be dfs(i+2) — a function CALL, not indexing
        #                              # dfs is a function, not subscriptable — this would crash

        #     dp[i] = res
        #     return res

        # return dfs(0)