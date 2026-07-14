class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # Key Data Structure: Two Pointer

        # Sort our array
        nums.sort()
        n = len(nums)
        res = []

        # Iterate through each number
        for i in range(n):

            # Optimizer
            if nums[i] > 0:
                break

            # If we run into the same number
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Pointers to track sums
            lo, hi = i+1, n-1

            # Find Targets 
            while lo < hi:
               
                # Check the sum first
                summ = nums[i] + nums[lo] + nums[hi]

                # If sum equals 0
                if summ == 0:

                    # Append to out result
                    res.append((nums[i],nums[lo],nums[hi]))

                    # Update the Pointers
                    lo += 1
                    hi -= 1

                    # Ensure we dont have duplicate Pointers
                    while lo < hi and nums[lo] == nums[lo - 1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi + 1]:
                        hi -= 1

                # Otherwise update pointers normally
                else:
                    if summ > 0:
                        hi -= 1
                    elif summ < 0:
                        lo += 1

        return res
        