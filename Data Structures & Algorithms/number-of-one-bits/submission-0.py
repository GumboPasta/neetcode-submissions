class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        binary_str = format(n & 0xFFFFFFFF, '032b')
        for i in range(len(binary_str)):
            if binary_str[i] == "1" :
                count += 1

        return count