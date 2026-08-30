class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        # Key Data Structure: Math / Bit Manipulation
        n = len(nums)
        res = n  # start with n itself (accounts for the "extra" expected index)
       
        for i in range(n):
            # for each index i, add (i - nums[i]) to res
            # this effectively computes: sum(expected indices) - sum(actual values)
            res += (i - nums[i])

        return res  # whatever's left over is the missing number

        # Time Complexity:  O(n) — single pass through nums
        # Space Complexity: O(1) — just a running total