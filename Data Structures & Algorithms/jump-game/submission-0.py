class Solution:
    def canJump(self, nums: List[int]) -> bool:

        # Key Data Structure: Greedy (Backward Traversal)

        n = len(nums)
        target = n - 1  # the goal we're trying to reach — starts as the actual last index

        # walk backwards from the end of the array
        for i in range(n - 1, -1, -1):
            max_jump = nums[i]  # max steps we can jump from index i

            # if jumping from i can reach (or pass) the current target,
            # then i itself becomes the new target — we now just need to
            # figure out if we can reach i from somewhere earlier
            if i + max_jump >= target:
                target = i

        # if target got reduced all the way down to 0, that means
        # index 0 (the start) can reach the goal through some chain of jumps
        return target == 0

        # Time Complexity:  O(n) — single backward pass through the array
        # Space Complexity: O(1) — only tracking a single variable