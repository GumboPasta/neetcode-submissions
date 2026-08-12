class Solution:
    def rob(self, nums: List[int]) -> int:

        # Key Data Structure: Dynamic Programming

        if len(nums) == 1:
            return nums[0]  # edge case: only one house, no circular conflict possible

        def rob_linear(houses):
            prev, curr = 0, 0
            for num in houses:
                prev, curr = curr, max(num + prev, curr)
            return curr

        # exclude last house, or exclude first house — take the better result
        return max(
            rob_linear(nums[:-1]),   # scenario A: houses 0 to n-2
            rob_linear(nums[1:])     # scenario B: houses 1 to n-1
        )

        # Time Complexity:  O(n) — two linear passes over the array
        # Space Complexity: O(1) — no extra array, just tracking two variables