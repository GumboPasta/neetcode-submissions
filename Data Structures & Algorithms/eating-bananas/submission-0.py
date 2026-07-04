from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # Key Data Structure: Binary Search

        def k_works(k):
            hours = 0
            for p in piles:
                hours += ceil(p / k)  # hours needed for this pile at speed k

            return hours <= h  # valid if total hours fits within h

        l = 1           # minimum possible speed
        r = max(piles)  # maximum needed speed (finish largest pile in 1 hour)

        while l < r:  # < not <=, since we're converging on the minimum valid k
            k = (l + r) // 2
            if k_works(k):
                r = k      # k is valid, but a smaller speed might also work
            else:
                l = k + 1  # k is too slow, discard left half

        return r  # l == r, the minimum valid speed

        # Time Complexity: O(n * log(max(piles))) — log(max) binary search steps, O(n) check each
        # Space Complexity: O(1)