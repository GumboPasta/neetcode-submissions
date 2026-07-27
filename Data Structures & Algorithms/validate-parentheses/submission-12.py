class Solution:
    def isValid(self, s: str) -> bool:

        # Key Data Structure: Stack
        
        charMap = {"}":"{","]":"[",")":"("}
        stk = []
        n = len(s)

        for i in range(n):

            # If it is a closing character
            if s[i] in charMap:
                # If stk is not empty and the top value is equal to the opening character
                if stk and stk[-1] == charMap[s[i]]:
                    stk.pop()
                else:
                    return False

            else:
                stk.append(s[i])

        return True if not stk else False
                
        

        