from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Key Data Structure: HashMap
        freq = defaultdict(list)

        # Iterate through our List
        for word in strs:

            count = [0] * 26
            # Iterate though each character in word
            for char in word:
                # Count the frequency in of each letter
                count[ord(char) - ord('a')] += 1

            # Store the count as the key (Must be immutable) and Value is a list of the group of anagrams
            freq[tuple(count)].append(word)
        
        # Return our result as a list
        return list(freq.values())

        # Time Complexity: O(m * n)
        # Space Complexity: O(n)