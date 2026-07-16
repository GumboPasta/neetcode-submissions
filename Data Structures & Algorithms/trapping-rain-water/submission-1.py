class Solution:
    def trap(self, height: List[int]) -> int:

        # Key Data Structure: Two Pointers

        # Store Max Wall Heights for each index
        n = len(height)
        l_wall = [0] * n
        r_wall = [0] * n

        # Track Max Heights
        max_left = 0
        max_right = 0
        res = 0

        # Fill our arrays
        for i in range(n):
            j = -i - 1

            # Store max height of walls
            l_wall[i] = max_left
            r_wall[j] = max_right

            # Keep track of our max values (Compare current value)
            max_left = max(max_left, height[i])
            max_right = max(max_right, height[j])
        print(l_wall)
        print(r_wall)
            
        # Obtain the max water area
        summ = 0
        for i in range(n):
            # Use the minimum height
            pot = min(l_wall[i],r_wall[i])
            summ += max(0, pot - height[i])


        return summ


        