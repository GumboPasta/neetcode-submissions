class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        sol = []
        n = len(nums)

        # helper function: perform dfs and backtracking
        def backtrack(i, cur_sum):
            # base case: dead scenario
            if cur_sum > target or i == n:
                return

            # if we have a matched cur_sum
            if cur_sum == target:
                res.append(sol.copy())
                return

            # first choice: skip the number
            backtrack(i+1, cur_sum)

            # second choice: include the number
            sol.append(nums[i])
            backtrack(i, cur_sum + nums[i])

            # redo our choice
            sol.pop()
            

        backtrack(0,0)
        return res
