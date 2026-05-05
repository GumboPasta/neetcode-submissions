class Solution:

    def encode(self, strs: List[str]) -> str:
        # Use '#' as delimiter and keep track of each length of string
        res = ''
        for string in strs:
            res += str(len(string)) + '#' + string
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
      

        while i < len(s):
            j = i

            # Obtain the length
            while s[j] != '#':
                j += 1
            length = s[i:j]

            # Append to result
            res.append(s[j+1:j+1+int(length)])
            
            # Update pointers
            i = j + int(length) + 1
            j = i

    
        return res
