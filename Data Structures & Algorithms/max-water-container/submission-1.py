class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # Key Data Structure: Hash Set 
        n = len(heights)
        lo = 0
        hi = n - 1
        max_area = 0

        while lo < hi:

            # Obtain the lowest height
            height = min(heights[lo], heights[hi])
            width = hi - lo
            area = height * width
            max_area = max(max_area, area)

            # Update our pointers (Move the shortest height pointer)
            if heights[lo] < heights[hi]:
                lo += 1
            else:
                hi -= 1

        return max_area

        # Time Complexity: O(n)
        # Space Complexity: O(1)
        