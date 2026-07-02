class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # Key Data Structure: Binary search

        left = 0
        right = len(nums) - 1

        while left <= right:  # <= because a window of 1 element is still valid
            middle = (right + left) // 2

            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                right = middle - 1  # target is smaller, discard right half
            else:
                left = middle + 1  # target is bigger, discard left half

        return -1  # left > right means window is empty, target not present

        # Time Complexity: O(log(n)) — search space halves each iteration
        # Space Complexity: O(1) — just two pointers, no extra structures