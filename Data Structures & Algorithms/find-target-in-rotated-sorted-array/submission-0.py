class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # Key Data Structure: Binary Search

        n = len(nums)
        l = 0 
        r = n - 1

        # Phase 1: find the index of the minimum element (the rotation pivot)
        while l < r:
            m = (l + r) // 2

            if nums[m] > nums[r]:
                l = m + 1  # min is in the right half
            else:
                r = m      # min is at m or to the left

        min_i = l  # l converged on the pivot (smallest element)

        # Phase 2: decide which sorted half the target lives in
        if min_i == 0:
            l, r = 0, n - 1          # array isn't rotated, search everything
        elif target >= nums[0] and target <= nums[min_i - 1]:
            l, r = 0, min_i - 1      # target is in the left sorted half
        else:
            l, r = min_i, n - 1      # target is in the right sorted half

        # Phase 3: standard binary search on the chosen half
        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return -1  # target not found

        # Time Complexity: O(log n) — two binary searches, both O(log n)
        # Space Complexity: O(1) — just pointers, no extra structures