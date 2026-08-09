class Solution:
    def climbStairs(self, n: int) -> int:

        # Key Data Structure: Dynamic Programming (Bottom-Up, Space Optimized)

        if n == 1:
            return 1  # only 1 way to climb 1 step
        if n == 2:
            return 2  # 2 ways to climb 2 steps: (1+1) or (2)

        prev = 1  # ways to reach step (i-1) — starts as ways to reach step 1
        cur = 2   # ways to reach step i — starts as ways to reach step 2

        # walk forward from step 3 up to step n
        # at each step: ways to reach current step = ways to reach the two steps before it
        for i in range(2, n):
            prev, cur = cur, prev + cur  # shift window forward: prev becomes old cur, cur becomes their sum

        return cur  # after the loop, cur holds the answer for step n

        # Time Complexity:  O(n) — single pass from step 3 to step n
        # Space Complexity: O(1) — only two variables tracked, no array needed