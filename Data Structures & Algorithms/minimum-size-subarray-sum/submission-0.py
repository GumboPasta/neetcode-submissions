class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        n = len(nums)
        l = 0
        res = float('inf')
        curr_sum = 0

        # iterate through our array
        for r in range(n):

            # update current sum
            curr_sum += nums[r]
        
            # shorten our window: we reached our target
            while curr_sum >= target:
                print(curr_sum,res)
                # track minimum length
                res = min(res, r - l + 1)
                # decrease sum and move left pointer
                curr_sum -= nums[l]
                l += 1

        if res == float('inf'):
            return 0
        return res
      
