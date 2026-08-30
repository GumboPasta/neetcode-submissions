class Solution:
    def reverseBits(self, n: int) -> int:

        # Key Data Structure: Bit Manipulation

        res = 0  # accumulates the reversed 32-bit result

        for i in range(32):
            # extract the bit at position i from n:
            # shift n right by i so that bit lands in the lowest position,
            # then mask with & 1 to isolate just that single bit
            bit = (n >> i) & 1

            # place that bit into the MIRRORED position in res:
            # bit at position i (from the right) in n
            # becomes bit at position (31 - i) in res
            res = res | (bit << (31 - i))

        return res

        # Time Complexity:  O(1) — always exactly 32 iterations, fixed bit-width
        # Space Complexity: O(1) — just a few integer variables