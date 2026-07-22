class Solution:
    def isValid(self, s: str) -> bool:
        

        # Key Data Structure: Stack

        validParenth = {")":"(","}":"{","]":"["}
        stk = []


        for char in s:

            if char in validParenth:
                if stk and stk[-1] == validParenth[char]:
                    stk.pop()
                else: 
                    return False

            else:
                stk.append(char)
           

        return True if not stk else False


