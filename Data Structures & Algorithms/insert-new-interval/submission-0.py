class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        # Key Data Structure: Interval Merging (Greedy Scan)

        n = len(intervals)
        res = []

        start = 0  # start index within each interval
        end = 1    # end index within each interval

        for i in range(n):
            if newInterval[end] < intervals[i][start]:
                # newInterval ends before this interval starts — no more overlaps possible
                res.append(newInterval)
                return res + intervals[i:]

            elif newInterval[start] > intervals[i][end]:
                # newInterval starts after this interval ends — no overlap, keep as-is
                res.append(intervals[i])

            else:
                # overlapping — merge into the widest possible range
                newInterval = [
                    min(newInterval[start], intervals[i][start]),
                    max(newInterval[end], intervals[i][end])
                ]

        res.append(newInterval)  # append merged interval (belongs after everything else)
        return res

        # Time Complexity:  O(n) — single pass through intervals
        # Space Complexity: O(n) — result list