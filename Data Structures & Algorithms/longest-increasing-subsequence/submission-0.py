class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # Key Data Structure: Dynamic Programming (Bottom-Up)

        n = len(nums)
        dp = [1] * n  # dp[i] = length of longest increasing subsequence ENDING at index i
                       # every element is at minimum a subsequence of length 1 (itself)

        for i in range(1, n):
            for j in range(i):
                # if nums[j] is smaller, we could extend the subsequence ending at j
                # by appending nums[i] to it
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)  # longest subsequence found, ending anywhere in the array

        # Time Complexity:  O(n^2) — nested loop, checking every pair (i,j)
        # Space Complexity: O(n) — dp array of size n