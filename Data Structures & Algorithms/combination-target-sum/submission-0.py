class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        # Key Data Structure: Backtracking

        res, sol = [], []  # res = all valid combinations, sol = current combination being built
        n = len(nums)

        def backtrack(i, cur_sum):
            if cur_sum == target:
                res.append(sol[:])  # found valid combination — append a copy (not reference)
                return

            if cur_sum > target or i == n:
                return  # exceeded target or ran out of numbers — dead end, backtrack

            # choice 1: SKIP nums[i] — move to next number without adding it
            backtrack(i + 1, cur_sum)

            # choice 2: INCLUDE nums[i] — add it to current combination
            sol.append(nums[i])
            backtrack(i, cur_sum + nums[i])  # stay at i (can reuse same number)
            sol.pop()  # undo the choice — backtrack

        backtrack(0, 0)
        return res

        # Time Complexity:  O(2^(t/m)) — t=target, m=minimum number in nums
        # Space Complexity: O(t/m) — max recursion depth (keep picking smallest number)