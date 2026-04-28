class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # Key Data Structure: Two Pointers

        # Base Case:
        if len(s) == 0:
            return False

        # Create two pointers (Start and End)
        i = 0
        j = len(s) - 1
        
        # Loop until pointers collide
        while i < j:
          
            # First check if the current character 'i' is alphanumeric
            if not s[i].lower().isalnum():
                i += 1
                continue
           
            # First check if the current character 'j' is alphanumeric
            if not s[j].lower().isalnum():
                j -= 1
                continue

            # Check if our values equal
            if s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else:
                return False

        return True

        # Time Complexity: O(n)
        # Space Complexity: O(n)
            