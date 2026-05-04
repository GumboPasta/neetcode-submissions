class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        # Key Data Structure: Two Pointer

        n = len(heights)
        lo = 0
        hi = n - 1
        max_area = 0

        # Iterate while pointers do not meet
        while lo < hi:

            # Calculate the area
            width = hi - lo
            height = min(heights[lo], heights[hi])
            area = width * height
            max_area = max(max_area, area)

            # Update pointers
            if heights[lo] < heights[hi]:
                lo += 1
            else:
                hi -= 1

        # Return max
        return max_area

        # Time Complexity: O(n)
