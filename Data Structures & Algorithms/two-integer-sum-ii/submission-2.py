class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # Key Data Structure: Two Pointers

        left = 0
        right = len(numbers) - 1

        while left < right:

            # Check current sum
            if numbers[left] + numbers[right] == target:
                return [left+1,right+1]

            # If sum is too big
            if numbers[left] + numbers[right] > target:
                right -= 1
           
            # If sum is too small
            if numbers[left] + numbers[right] < target:
                left += 1

        return []

        