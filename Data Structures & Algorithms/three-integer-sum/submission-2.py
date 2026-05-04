class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # Key Data Structure: Two Pointers

        # Sort the array by least to greatest
        nums.sort()
        n = len(nums)
        res = []

        # Iterate through each unique index
        for i in range(n):

            # Optimizer: If current number is greater than 0 means sum will always be greater than 0
            if nums[i] > 0:
                break

            # Optimizer: If the current index and last index index are the same, skip iteration
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Set the pointers
            lo, hi = i+1, n-1

            while lo < hi:

                # Obtain the sum of all three numbers
                summ = nums[i] + nums[lo] + nums[hi]

                if summ == 0:

                    # Add combo to result
                    res.append([nums[i],nums[lo], nums[hi]])

                    # Update pointers
                    lo += 1
                    hi -= 1

                    # Make sure each of the pointers are new numbers
                    while lo < hi and nums[lo] == nums[lo-1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi+1]:
                        hi -= 1

                else:
                    
                    # Update the pointer based on the sum
                    if summ < 0:
                        lo += 1
                    if summ > 0:
                        hi -= 1

        return res
        



                








        
        