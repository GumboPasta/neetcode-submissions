class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Key Data Structure: Sliding Window

        window = []
        buy = 0
        sell = 1
        n = len(prices)
        max_profit = 0

        while sell < n:

            # Obtain profit and store max profit
            profit = prices[sell] - prices[buy]
            max_profit = max(max_profit, profit)

            # Update the window
            if prices[sell] < prices[buy]:
                buy = sell

            sell += 1

        return max_profit

        # Time Complexity: O(n)
        # Space Complextity: O(1)
        