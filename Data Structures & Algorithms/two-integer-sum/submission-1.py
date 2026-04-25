class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Key Data Structure: Hashmap
        
        # Create the hashmap {uniqueValue:Index}
        hashMap = {}

        for i in range(len(nums)):

            neededSum = target - nums[i]
            # Check if the neededSum is in hashmap already
            if neededSum in hashMap:
                return [hashMap[neededSum], i]

            # Otherwise add the value to hashmap
            hashMap[nums[i]] = i

        return []


    # Time Complexity: O(n)
    # Space Complexity: O(n)
        