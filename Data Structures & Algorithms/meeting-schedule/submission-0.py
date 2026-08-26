class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        # Key Data Structure: Interval Sorting (Sort + Single Pass)

        intervals.sort(key=lambda intervals: intervals.start)  # sort by meeting start time

        for i in range(1, len(intervals)):
            i1 = intervals[i - 1]  # the previous meeting
            i2 = intervals[i]      # the current meeting

            # if the previous meeting ends AFTER the current one starts,
            # they overlap — can't attend both
            if i1.end > i2.start:
                return False

        return True  # no overlaps found — every meeting is attendable

        # Time Complexity:  O(n log n) — dominated by the sort
        # Space Complexity: O(1) — excluding the sort's internal space