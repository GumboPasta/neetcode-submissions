class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # Key Data Structure: Sliding Window

        n = len(s)
        l = 0
        window = []
        dupeTracker = set()
        max_size = 0

        # Iterate through each number
        for i in range(n):

            # Check if current character is in window
            if s[i] in dupeTracker:

                # Move the left pointer until we dont have a duplicate in our window
                while s[i] in dupeTracker:
                    dupeTracker.remove(s[l])
                    l += 1

            max_size = max(max_size, i - l + 1)
            dupeTracker.add(s[i])

        return max_size
            

            


                
                
        