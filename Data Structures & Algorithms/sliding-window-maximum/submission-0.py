class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        # Key Data Structure: Sliding Window with Deque

        output = []
        q = deque() # Store indexes
        l = r = 0

        while r < len(nums):
            
            # While the right most number in the deque is still smaller than current number
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # Make sure deque only includes our window
            if l > q[0]:
                q.popleft()
            
            # If we have met the length our window, add to result and increment left pointer
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output

        # Time Complexity: O(n)
        # Space Complexity: O(n)