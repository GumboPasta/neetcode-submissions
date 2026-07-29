class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # Key Data Structure: Sliding Window
        n = len(s)
        window = []
        l = 0
        res = 0

        # Track freq of each character
        count = [0] * 26

        # Iterate through the string
        for r in range(n):
            count[ord(s[r]) - ord("A")] += 1
            
            # Loop (While (Window Length - Highest Freq Character) > # of Replacements
            while (r - l + 1) - max(count) > k:
                count[ord(s[l]) - ord("A")] -= 1
                l += 1
            
            res = max(res, (r-l+1))
        

        
        return res

        # [A,B,A,B,B]
        # res = 6
