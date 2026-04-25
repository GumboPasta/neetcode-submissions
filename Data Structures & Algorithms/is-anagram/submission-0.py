class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # If two string are an anagram it means the same letters are present and same number of letters

        # Lets sort both of the strings in alphabetical order
        sortedS = "".join(sorted(s))
        sortedT = "".join(sorted(t))

        if sortedS != sortedT:
            return False

        return True        










        # 1st Solution: Order the strings by alphabetical order and then compare the values in a loop iteration (Onlog(n))
        # Best Solution: 