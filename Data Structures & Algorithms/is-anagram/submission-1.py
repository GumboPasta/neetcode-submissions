class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # If two string are an anagram it means the same letters are present and same number of letters

        # Base Check: If length of strings match each other
        if len(s) != len(t):
            return False

        # Create the Hashmap to store the frequencies
        mapS, mapT = {}, {}

        for i in range(len(s)):

            # Increment and store the frequencies of each letter
            mapS[s[i]] = 1 + mapS.get(s[i], 0)
            mapT[t[i]] = 1 + mapT.get(t[i], 0)

        return mapS == mapT











        # 1st Solution: Order the strings by alphabetical order and then compare the values in a loop iteration (Onlog(n))
        # Best Solution: Is to use hashmap to track the frequencies of each of the letters