class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # Key Data Structure: Binary Search

        n = len(nums)
        l = 0
        r = n - 1

        while l < r:  # < not <=, when l == r we've found the minimum
            m = (l + r) // 2

            if nums[m] > nums[r]:
                # m is in the clean left half, minimum must be to the right
                l = m + 1
            else:
                # m is in the rotated right half, minimum is at m or to the left
                r = m  # not m-1, m itself could be the minimum

        return nums[l]  # l == r, converged on the minimum

        # Time Complexity: O(log n) — search space halves each iteration
        # Space Complexity: O(1) — just two pointers, no extra structures