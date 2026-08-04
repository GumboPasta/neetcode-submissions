class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # Key Data Structure: Binary Search
        n = len(nums)
        l, r = 0, n - 1
        res = 0

        # While left and right pointers dont equal
        while l < r:
            
            # Obtain the middle value
            m = (r + l) // 2
            print(l,r,m)
            # Two conditions: If the middle is greater than the right
            if nums[m] > nums[r]: # Means the drop is in the right side
                l = m + 1
            else: # Means the drop is in the left side
                r = m # Set it to m because it can be m

        return nums[l]