import heapq

class MedianFinder:

    # Key Data Structure: Two Heaps (Max Heap + Min Heap)

    def __init__(self):
        self.small_nums = []  # max heap (lower half) — values stored negated
        self.large_nums = []  # min heap (upper half)

    def addNum(self, num: int) -> None:
        # step 1: always push to small (max heap) first
        heapq.heappush(self.small_nums, -num)

        # step 2: always move small's top to large
        # this guarantees every element in small <= every element in large
        heapq.heappush(
            self.large_nums,
            -heapq.heappop(self.small_nums)
        )

        # step 3: rebalance if large has more elements than small
        # small is allowed to have at most 1 more element than large (odd total)
        # but large should never have more than small
        if len(self.small_nums) < len(self.large_nums):
            heapq.heappush(
                self.small_nums,
                -heapq.heappop(self.large_nums)
            )

    def findMedian(self) -> float:
        # odd total — small has 1 extra element, that's the median
        if len(self.small_nums) > len(self.large_nums):
            return -self.small_nums[0]

        # even total — median is average of both heap tops
        return (
            -self.small_nums[0] + self.large_nums[0]
        ) / 2.0

        # Time Complexity:  O(log n) addNum — heap push/pop
        #                   O(1) findMedian — peek at heap tops
        # Space Complexity: O(n) — storing all n numbers across both heaps