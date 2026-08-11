class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # Bottom Up DP (Constant Space)
        # Time: O(n)
        # Space: O(1)

        n = len(nums)
        if n == 1:
            return nums[0]  # only one house, must rob it
        if n == 2:
            return max(nums[0], nums[1])  # two houses, take the bigger one

        prev = nums[0]                      # best result up to house (i-2), starts as house 0
        curr = max(nums[0], nums[1])        # best result up to house (i-1), starts as best of houses 0,1

        for i in range(2, n):
            # rob nums[i] + best up to (i-2)   vs   skip it, keep best up to (i-1)
            prev, curr = curr, max(nums[i] + prev, curr)

        return curr  # curr holds the best result after processing all houses

        # ⚠️ NOTE: everything below this point is unreachable code —
        # the function already returned above, so this never executes.
        # Keeping it here only as reference/scratch notes for the alternate approach.

        # Top Down DP (Memoization) Approach: -> (However Recursion is slower)
        # Time: O(n)
        # Space: O(n)

        # n = len(nums)
        # if n == 1:
        #     return nums[0]
        # if n == 2:
        #     return max(nums[0], nums[1])

        # memo = {0: nums[0], 1: max(nums[0], nums[1])}  # base cases pre-filled

        # def helper(i):
        #     if i in memo:
        #         return memo[i]              # already computed, return cached result
        #     else:
        #         # rob house i + best up to (i-2)   vs   skip house i, best up to (i-1)
        #         memo[i] = max(nums[i] + helper(i-2), helper(i-1))
        #         return memo[i]

        # return helper(n-1)