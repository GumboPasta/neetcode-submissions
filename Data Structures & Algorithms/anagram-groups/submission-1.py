class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Key Data Structure: Hashmap

        # Create Hashmap {anagram : list of strings} - Default value for the map is list
        storedAnagrams = defaultdict(list)

        for str in strs:
            # Create a list of 0's to track letter counts
            count = [0] * 26 # a...z

            # Iterate through the string to increment frequencies
            for char in str:
                count[ord(char) - ord("a")] += 1

            # Add to hashmap
            storedAnagrams[tuple(count)].append(str)

        return list(storedAnagrams.values())

        # Time Complexity: O(n * m) where n is the length of strs, and m is the average length of each str



        