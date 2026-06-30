class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair positions with speeds
        pair = [(p, s) for p, s in zip(position, speed)]

        # Process front-to-back (closest to target first)
        pair.sort(reverse=True)

        stack = []  # arrival times of current fleet leaders

        for p, s in pair:
            time_to_target = (target - p) / s
            stack.append(time_to_target)

            # Catches the fleet ahead -> merges, don't count separately
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)  # one entry per distinct fleet