class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # Hashmap [Key] : Value | [Value] : Index of the element
        result = {}

        # Iterate through the list
        for index, number in enumerate(nums):
            # Calculate the needed number by subtracting current element from target
            neededNumber = target - number

            # First check if the needed number is in the list
            if neededNumber in result:
                # If present return the current index plus the others elements index
                return [result[neededNumber], index]
            # Otherwise add the element to the map
            result[number] = index



# Example
# nums = [2,7,11,15], target = 9
# First iteration: [2] -> result: [2:0]
# Second iteration: [2,7] -> output:[0,1]
        