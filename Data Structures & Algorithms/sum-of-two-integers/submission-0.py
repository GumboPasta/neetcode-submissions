class Solution:
    def getSum(self, a: int, b: int) -> int:

        # Key Data Structure: Bit Manipulation

        mask = 0xFFFFFFFF     # 32 ones — used to truncate results to 32 bits
                               # (Python ints are unbounded, so this simulates 32-bit overflow)
        max_int = 0x7FFFFFFF  # largest positive 32-bit signed int (2^31 - 1)

        while b != 0:
            # carry = bits where BOTH a and b have a 1 (these produce a carry in addition)
            # shift left by 1 since a carry always affects the NEXT higher bit position
            carry = (a & b) << 1

            # a ^ b adds the bits WITHOUT carrying (XOR mimics addition ignoring overflow)
            # mask keeps the result within 32 bits
            a = (a ^ b) & mask

            # the carry becomes the new "b" to be added in on the next iteration
            # (keep repeating until there's no carry left to add)
            b = carry & mask

        # if a fits within a positive 32-bit signed range, return it directly
        # otherwise, it represents a negative number in 32-bit two's complement,
        # so convert it back to Python's native (unbounded) negative representation
        return a if a <= max_int else ~(a ^ mask)

        # Time Complexity:  O(1) — bounded by 32 bit positions maximum
        # Space Complexity: O(1) — just a few integer variables