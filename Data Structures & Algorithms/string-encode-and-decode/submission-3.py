class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            result += str(len(word)) + "#" + word
        return result

    def decode(self, s: str) -> List[str]:

        result, i = [], 0

        while i < len(s):
            j = i
            # Keeps track of the delimiter
            while s[j] != '#':
                j += 1
            # Once delimiter is found keep track of the length
            length = int(s[i:j])

            # Add the word
            result.append(s[j+1:j+1+length])

            # Update the pointer
            i = j+1+length

        return result


    # The delimiter is used to keep track of the end of the length in the string (Reads the length)
    # Example: 
    # 4#neet4#code4#love3#you