class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # Key Data Structure: Sliding Window
    
        n1 = len(s1)
        n2 = len(s2)

        # Base Case: If our permutation string length is bigger than substring
        if n1 > n2:
            return False
        
        s1_counts = [0] * 26
        s2_counts = [0] * 26

        # Build intial sliding window
        for i in range(n1):
            s1_counts[ord(s1[i]) - ord('a')] += 1
            s2_counts[ord(s2[i]) - ord('a')] += 1

        # Base Case: If intial sliding window is already correct
        if s1_counts == s2_counts:
            return True
        
        # Iterate and move our sliding window in the remaining letters
        for i in range(n1, n2):
            # Increment our right window count and decrement our left window
            s2_counts[ord(s2[i]) - ord('a')] += 1
            s2_counts[ord(s2[i-n1]) - ord('a')] -= 1
            # Check if they ever equal
            if s1_counts == s2_counts:
                return True

        return False

        # Time Complexity: O(n1) + O(n2) or O(n2) since it is bigger
        # Space Complexity: O(1)

