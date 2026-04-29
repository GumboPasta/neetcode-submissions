class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # Example: nums = [1,2,4,6]

        # Left Product: [1,1,2,8] -> Prefix at each index meaning, if i am at index = 3, the prefix is just 1x2x4 =  8
        # Right Product: [48,24,6,1] -> Postfix

        # Base Check
        if len(nums) == 0:
            return []

        # Create empty arrays
        prefix = [0] * len(nums)
        postfix = [0] * len(nums)

        # Assigns 1's for the prefix and postfix for the 1st and last values since they dont have a number next to them
        left = 1
        right = 1

        for i, num in enumerate(nums):

            # Assign intial prefix
            prefix[i] = left 

            # Assign the last position in the array
            j = -i - 1
            postfix[j] = right

            # Update next products
            left *= nums[i]
            right *= nums[j]

        # Take each pair of numbers from prefix and postfix, multiple them, and return the list of results"
        return [l*r for l,r in zip(prefix, postfix)]
