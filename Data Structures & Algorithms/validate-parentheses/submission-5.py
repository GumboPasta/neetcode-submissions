class Solution:
    def isValid(self, s: str) -> bool:

        # Key Data Structure: Stack
        stack = []

        # Create a map for each closing character
        mapping = {"}":"{",")":"(","]":"["}

        # Iterate through the list
        for i in range(len(s)):
        
            # If character is a closing character
            if s[i] in mapping:
                # Peek if match is the top of stack
                if stack and stack[-1] == mapping[s[i]]:
                    stack.pop()
                else:
                    return False

            # Add to opening character to stack
            else:
                stack.append(s[i])
        
        return True if not stack else False

        # Time Complexity: O(n)
        # Space Complexity: O(n)
                

        