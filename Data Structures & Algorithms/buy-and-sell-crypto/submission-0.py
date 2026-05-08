class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Key Data Structure: Stack
        stack = []
        i = 0
        j = 1
        maxProfit = 0

        # Iterate through the list
        while j < len(prices):

            # Track the price
            profit = prices[j] - prices[i]
            maxProfit = max(maxProfit, profit)

            # If our profit is negative, move our buy day
            if profit < 0: 
                i = j
            
            # Increment j pointer
            j += 1
        
        # Return result
        return maxProfit
            
        # Time Complexity: O(n)
        # Space Complexity: O(1)







