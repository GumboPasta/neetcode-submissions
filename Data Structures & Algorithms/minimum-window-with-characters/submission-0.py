class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # Key Data Structure: Sliding Window

        if t == "":
            return ""

        # Track the counts of target using HashTable
        countT, window = {}, {}
        for character in t:
            countT[character] = 1 + countT.get(character, 0)

        # Key: Track Have and Need values to check if the actual target values are there, this removes the non-target values
        have, need = 0, len(countT)
        result, resLength = '', float("infinity")
        l = 0
        n = len(s)

        # Iterate through our loop
        for r in range(n):
            
            # Increment our arrayCount
            character = s[r]
            window[character] = 1 + window.get(character, 0)

            # If it is part of a target and meets the count
            if character in countT and window[character] == countT[character]:
                have += 1

            # If substring is met
            while have == need:
                # Keeps track of smallest substring
                if (r - l + 1) < resLength:
                    result = s[l:r+1]
                    resLength = r - l + 1

                # Decrement count and move pointer
                window[s[l]] -= 1

                # Decrement our trackers
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1

                l += 1

        return result 

            





        