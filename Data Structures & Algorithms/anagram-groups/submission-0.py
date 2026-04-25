class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Key Data Structure: Hashmap

        # Create Hashmap {anagram : list of strings}
        storedAnagrams = {}

        for str in strs:

            # Lets sort the string alphabetically
            sortedStr = "".join(sorted(str))

            # Add to Hashmap
            storedAnagrams[sortedStr] = storedAnagrams.get(sortedStr,[]) + [str]


        return list(storedAnagrams.values())

        