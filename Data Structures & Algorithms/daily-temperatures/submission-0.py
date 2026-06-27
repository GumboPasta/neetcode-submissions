class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        temps = temperatures
        n = len(temps)
        answer = [0] * n  # Default 0 means "no warmer day found"
        stk = []  # Monotonic decreasing stack storing (temperature, index) pairs

        for i, t in enumerate(temps):
            # Current temp is warmer than stack top — resolve waiting days
            while stk and stk[-1][0] < t:
                stk_t, stk_i = stk.pop()
                answer[stk_i] = i - stk_i  # Days waited = current index - stored index

            # Push current day; it's now waiting for its own warmer day
            stk.append((t, i))

        # Any indices still in stack never found a warmer day → answer stays 0
        return answer

        # Time: O(n) — each index is pushed and popped at most once
        # Space: O(n) — stack holds at most n elements