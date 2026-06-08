class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # Key Data Structure: Array

        # Store prefix and postfix products
        prefix = []
        postfix = []
        result = []
        n = len(nums)

        # Initial
        left = right = 1
        

        # Populate our initial product
        for i in range(n):

            # Assign products
            prefix.append(left)
            postfix.append(right)

            # Obtain next product
            left *= nums[i]
            right *= nums[-i-1]
      
        # Obtain the result Array
        for i in range(n):
            product = prefix[i] * postfix[-i - 1]
            result.append(product)

        return result

        # Time Complexity: O(n)
        # Space Complexity: O(n)