from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Key Data Structure: Hash Map

        freqMap = defaultdict(list)

        # Iterate through the List
        for word in strs:

            # Create a character frequency array
            charArray = [0] * 26

            for character in word:
                charArray[ord(character) - ord('a')] += 1

            # Add to the malistp
            freqMap[tuple(charArray)].append(word)

        print(freqMap)
        return list(freqMap.values())


        