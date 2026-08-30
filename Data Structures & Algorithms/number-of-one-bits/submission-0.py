class Solution:
    def hammingWeight(self, n: int) -> int:

        # Key Data Structure: Bit Manipulation

        ans = 0  # counts how many 1 bits we've found

        while n != 0:
            ans += 1          # found one set bit — count it
            n = n & (n - 1)   # clears the LOWEST set bit in n (see explanation below)

        return ans

        # Time Complexity: O(k) — k = number of 1 bits in n (not the total bit-width!)
        # Space Complexity: O(1) — just a counter