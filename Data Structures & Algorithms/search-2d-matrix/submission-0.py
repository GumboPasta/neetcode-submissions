class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # Key Data Structure: Binary Search

        rows = len(matrix)
        cols = len(matrix[0])
        total = rows * cols  # treat the matrix as a flat sorted array of length m*n
        l = 0
        r = total - 1

        while l <= r:  # <= because a window of 1 element is still valid
            mid = (l + r) // 2
            i = mid // cols  # convert flat index to row
            j = mid % cols   # convert flat index to column
            
            mid_num = matrix[i][j]

            if target == mid_num:
                return True
            elif target < mid_num:
                r = mid - 1  # target is smaller, discard right half
            else:
                l = mid + 1  # target is bigger, discard left half

        return False

        # Time Complexity: O(log(m*n)) — binary search over m*n virtual elements
        # Space Complexity: O(1) — just two pointers, no extra structures