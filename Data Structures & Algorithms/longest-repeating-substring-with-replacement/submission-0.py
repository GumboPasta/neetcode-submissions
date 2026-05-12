class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # Key Data Structure: Sliding Window
        longest = 0
        l = 0
        counts = [0] * 26

        for r in range(len(s)):
            counts[ord(s[r]) - ord('A')] += 1
            # If the longest - (max count in the array) is greater than the amount of characters I change
            # Means my window is invalid
            while (r-l+1) - max(counts) > k:
                counts[ord(s[l]) - ord('A')] -= 1
                l += 1

            longest = max(longest, (r-l+1))

        return longest

        # Time Complexity: O(n)
        # Space Complexity: O(1)