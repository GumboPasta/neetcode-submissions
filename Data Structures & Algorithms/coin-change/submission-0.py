class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # Key Data Structure: Dynamic Programming (Bottom-Up)
        # Time: O(coins * amount)
        # Space: O(amount)

        coins.sort()  # sort so we can safely break early once a coin is too big
        dp = [0] * (amount + 1)  # dp[i] = min coins needed to make amount i, dp[0]=0 by default

        # build up the answer for every amount from 1 to target
        for i in range(1, amount + 1):
            minn = float('inf')  # tracks best (fewest) coin count found for this amount

            for coin in coins:
                diff = i - coin  # amount remaining if we use this coin
                if diff < 0:
                    break  # coin too big for this amount — since sorted, all bigger coins are too, stop early

                # dp[diff] = min coins for the remainder, +1 for the coin we just used
                minn = min(minn, dp[diff] + 1)

            dp[i] = minn  # store the best result found for this amount

        # if dp[amount] is still infinity, no combination of coins could make it
        if dp[amount] < float('inf'):
            return dp[amount]
        else:
            return -1

        # Top Down DP (Memoization) — alternate approach, kept as reference
        # Time: O(coins * amount)
        # Space: O(amount)

        # coins.sort()
        # memo = {0: 0}  # base case: 0 coins needed to make amount 0

        # def min_coins(amt):
        #     if amt in memo:
        #         return memo[amt]  # already computed, return cached result

        #     minn = float('inf')
        #     for coin in coins:
        #         diff = amt - coin
        #         if diff < 0:
        #             break  # coin too big, sorted so all remaining are too
        #         minn = min(minn, 1 + min_coins(diff))  # recurse on the remainder

        #     memo[amt] = minn
        #     return minn

        # result = min_coins(amount)
        # if result < float('inf'):
        #     return result
        # else:
        #     return -1