class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # 1-index means that the array index starts at 1 instead of 0

        # Key Data Structure: Two Pointers

        # Have two pointers
        left = 0
        right = len(numbers) - 1

        # Iterate only if the two pointers do not meet each other
        while left < right: 
         
            # Obtain the sum 
            sum = numbers[left] + numbers[right]

            # Compare the sum and determine if it is less than or greater than the sum
            if sum == target:
                return [left+1,right+1]

            # If it is greater than the sum decrement my right pointer because it gurantees a smaller sum
            if sum < target:
                left += 1
            # Else if it is less than the sum increment my left pointer because it gurantees a bigger sum
            elif sum > target:
                right -= 1

        # Found no sum
        return []

        # Time Complexity: O(n)