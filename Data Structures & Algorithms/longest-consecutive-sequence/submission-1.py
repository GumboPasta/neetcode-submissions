class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # Key Data Structure: Hash Set

        s = set(nums)
        res = 0

        # Iterate through each number
        for num in nums:

            # Lets first check if its a start of a sequence
            if num-1 not in s:
                length = 1
                num += 1
                while num in s:
                    length += 1
                    num += 1
                res = max(length,res)
        
        return res

        # Time Complexity: O(n)
        # Space Complexity: O(n)

