class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # Key Data Structure: Sliding Window
        l = 0
        n = len(s)

        # Hashset to track duplicates
        duplicates = set()
        maxLength = 0

        # Iterate through the string
        for r in range(n):
        
            # If value is in set, remove and increment left window until it is not in set
            while s[r] in duplicates:
                duplicates.remove(s[l])
                l += 1
                
            # Obtain the length and keep track
            length = (r - l) + 1
            maxLength = max(maxLength, length)
            duplicates.add(s[r])
          
        return maxLength

        # Time Complexity: O(n)
        # Space Complexity: O(n)


        