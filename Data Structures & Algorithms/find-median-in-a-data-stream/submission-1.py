import heapq
class MedianFinder:

    # constructor method
    def __init__(self):
        self.small_nums = [] # maxheap
        self.large_nums = [] # minheap

    # add method
    def addNum(self, num: int) -> None:

        # add number first to maxheap
        heapq.heappush(self.small_nums, -num)

        # add the root number straight to minHeap to make sure smallNums <= large_nums
        heapq.heappush(self.large_nums, -heapq.heappop(self.small_nums))

        # make sure maxHeap is always greater than our minHeap
        if len(self.small_nums) < len(self.large_nums):
            # pop back to maxHeap
            heapq.heappush(self.small_nums, -heapq.heappop(self.large_nums))

    # find median method
    def findMedian(self) -> float:
        
        # if len is odd
        if (len(self.small_nums) != len(self.large_nums)):
            return -self.small_nums[0]

        # otherwise return the average of the 2 middle values
        return (-self.small_nums[0] + self.large_nums[0]) / 2
