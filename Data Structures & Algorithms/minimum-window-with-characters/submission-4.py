class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # Key Data Structure: Sliding Window
        
        # base case: if t is ever greater -> invalid
        if len(t) > len(s):
            return ""

        # two hashmaps: 1 to track window and 1 for count string T
        window, countT = {}, {}
        n = len(s)

        # populate our target hashmap
        for character in t:
            countT[character] = 1 + countT.get(character, 0)

        # trackers for valid substring
        have, need = 0, len(countT)
        l = 0
        res, resLength = "", float('inf')

        for r in range(n):

            # add to our window
            window[s[r]] = 1 + window.get(s[r], 0)

            # we have a valid part of string
            if s[r] in countT and window[s[r]] == countT[s[r]]:
                have += 1
           
            # handle whenever we have a valid substring
            while have == need:

                # keep track of our result
                if (r - l + 1) < resLength:
                    res = s[l:r+1]
                    resLength = (r - l + 1)

                # decrement window count
                window[s[l]] -= 1
                
                # update our trackers and pointers
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1

                l += 1

        return res


                









        

        

        
        