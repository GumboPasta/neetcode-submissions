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
            # Keep going until reach the delimiter (To find length of word)\
            while s[j] != '#':
                j += 1
            length = s[i:j] # Doesnt include delimiter
        
            # Append the word
            result.append(s[j+1:j+1+int(length)])

            # Update pointer (To next number)
            i = j+1+int(length)
            print(s)

        return result




# Example:
# 4#neet4#code4#love3#you