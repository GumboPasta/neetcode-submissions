class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        # Key Data Structure: Dynamic Programming (track running max AND min)

        res = max(nums)      # tracks the best product found overall
        curMin, curMax = 1, 1  # track running min/max product ending at the current position

        for n in nums:
            if n == 0:
                # a zero resets everything — any product including 0 is 0,
                # so start fresh from the next number
                curMin, curMax = 1, 1
                continue

            tmp = curMax * n  # save curMax*n before curMax gets overwritten below

            # why we need BOTH max and min:
            # a negative number can flip the smallest product into the largest
            # (and vice versa), so we must track both possibilities at every step
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(tmp, n * curMin, n)

            res = max(res, curMax)  # update global best whenever curMax improves

        return res

        # Time Complexity:  O(n) — single pass through the array
        # Space Complexity: O(1) — only a few tracking variables