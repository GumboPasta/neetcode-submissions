class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        # Key Data Structure: Greedy (Sort + Single Pass)

        intervals.sort(key=lambda intervals: intervals[0])  # sort by start time

        res = 0  # counts how many intervals need to be removed
        prevEnd = intervals[0][1]  # tracks the end of the last interval we're KEEPING

        for start, end in intervals[1:]:
            if start >= prevEnd:
                # no overlap — this interval is fine, keep it
                # update prevEnd to this interval's end going forward
                prevEnd = end
            else:
                # overlap detected — one of these two intervals must be removed
                res += 1  # count a removal

                # keep whichever interval ends EARLIEST, since it leaves more
                # room for future intervals to not overlap
                prevEnd = min(end, prevEnd)

        return res

        # Time Complexity:  O(n log n) — dominated by the sort
        # Space Complexity: O(1) — excluding the sort's internal space