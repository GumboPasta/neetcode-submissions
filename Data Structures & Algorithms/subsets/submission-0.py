class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        n = len(nums)

        def backtrack(index, curr_subset):
            
            # base case: if we reached a leaf
            if index == n:
                res.append(curr_subset.copy())
                return
           
            # first choice: skip the number
            backtrack(index + 1, curr_subset)

            # second choice: include the number
            curr_subset.append(nums[index])
            backtrack(index + 1, curr_subset)

            # undo the decision
            curr_subset.pop()

        backtrack(0, [])
        return res






        