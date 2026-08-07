class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # Key Data Structure: Binary Search
        n = len(nums)
        l, r = 0, n - 1
        res = 0

        # first binary search: determine minimum
        while l < r:
            m = (l + r) // 2

            if nums[m] > nums[r]: # minimum is in right half
                l = m + 1
            else:                 # minimum is in left half
                r = m
        min_index = l

        # determine which half target is in
        if nums[0] < nums[n - 1]:                                # case 1: if array is in same position -> normal binary search
            l, r = 0, n - 1
        elif target > nums[n - 1] and target <= nums[min_index - 1]: # case 2: if array is in left half
            l, r = 0, min_index - 1
        else: 
            l, r = min_index, n - 1
        print(min_index)
        print(l, r)
        # normal binary search
        while l <= r:
            m = (l + r) // 2
            print(m)
            if target == nums[m]:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        return -1