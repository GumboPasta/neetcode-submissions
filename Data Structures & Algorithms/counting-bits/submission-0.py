class Solution:
    def countBits(self, n: int) -> List[int]:

        # Key Data Structure: Dynamic Programming (Bit Manipulation)

        dp = [0] * (n + 1)  # dp[i] = number of 1 bits in the binary representation of i
        offset = 1           # tracks the most recent power of 2 (1, 2, 4, 8, ...)

        for i in range(1, n + 1):
            if offset * 2 == i:
                # i is exactly the next power of 2 — update offset to this new milestone
                # (e.g. offset was 1, now i=2 → offset becomes 2;
                #       offset was 2, now i=4 → offset becomes 4, etc.)
                offset = i

            # i's bit count = 1 (for the highest set bit, the "offset" bit)
            # + however many 1 bits are in (i - offset), the remaining lower bits
            dp[i] = 1 + dp[i - offset]

        return dp

        # Time Complexity:  O(n) — single pass, each dp[i] computed in O(1)
        # Space Complexity: O(n) — dp array of size n+1 (output itself)