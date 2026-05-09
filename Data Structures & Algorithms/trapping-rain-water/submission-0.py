class Solution:
    def trap(self, height: List[int]) -> int:
        
        l_wall = r_wall = 0
        n = len(height)
        max_left = [0] * n
        max_right = [0] * n

        for i in range(n):
            j = -i - 1

            # Analyze left and right wall arrays
            max_left[i] = l_wall
            max_right[j] = r_wall
            # Update maxes for both walls
            l_wall = max(l_wall, height[i])
            r_wall = max(r_wall, height[j])

        # Obtain the sum
        summ = 0
        for i in range(n):
            
            # Obtain potential water
            pot = min(max_left[i], max_right[i])
            summ += max(0, pot - height[i])

        return summ

        # Time Complexity: O(n)
        # Space Complexity: O(n)