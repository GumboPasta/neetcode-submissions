class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # Key Data Structure: Two Pointers

        # Sort out nums array
        nums.sort()
        n = len(nums)
        res = []
        

        # Iterate through each number
        for i in range(n):

            # Optimization: Since it is sorted anything to the right is greater than 0 as well
            if nums[i] > 0:
                break

            # Make sure current value is also not duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Each Iteration: Initialize Lo and Hi pointers
            lo, hi = i + 1, n - 1

            while lo < hi:
                # Calculate the sum of all three numbers
                summ = nums[i] + nums[lo] + nums[hi]
                
                # If sum = 0
                if summ == 0:
                    
                    # Append to our results array
                    res.append((nums[i],nums[lo],nums[hi]))

                    # Update our pointers 
                    lo += 1
                    hi -= 1

                    # Make sure both our pointers are new and not duplicates
                    while lo < hi and nums[lo] == nums[lo - 1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi + 1]:
                        hi -= 1

                # Else update pointers based sum
                else:
                    if summ > 0:
                        hi -= 1
                    else:
                        lo += 1

        return res



        