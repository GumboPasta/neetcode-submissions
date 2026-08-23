class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # Key Data Structure: Dynamic Programming / Greedy (Kadane's Algorithm)

        max_sum = float('-inf')  # tracks the best subarray sum found overall
        curr_sum = 0              # tracks the running sum of the current subarray

        for i in range(len(nums)):
            curr_sum += nums[i]           # extend the current subarray by including this number
            max_sum = max(max_sum, curr_sum)  # update global best if this is the new highest sum

            if curr_sum < 0:
                # a negative running sum can only hurt any future subarray —
                # reset to 0 so the next number starts a fresh subarray
                curr_sum = 0

        return max_sum

        # Time Complexity:  O(n) — single pass through the array
        # Space Complexity: O(1) — only two tracking variables