class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # Key Data Structure: Hash Set
        s = set(nums)
        longest = 0

        # Iterate through each number
        for num in nums:

            # Check if it is the start of a sequence
            if num - 1 not in s:
                length = 1
                nextNum = num + 1
                # Find the consecutive sequence
                while nextNum in s:
                    length += 1
                    nextNum += 1
                longest = max(longest, length)
        
        return longest

        # Time Complexity: O(n)
        # Space Complexity: O(n)



            
        