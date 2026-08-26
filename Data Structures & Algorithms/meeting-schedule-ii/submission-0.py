class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        # Key Data Structure: Two Pointers (Sorted Start/End Times)

        # separate all start times and all end times into their own sorted lists
        # (we lose track of which start belongs to which end — but that's okay,
        # we only care about the COUNT of overlapping meetings at any moment)
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        res, count = 0, 0  # res = max rooms needed at any point, count = rooms currently in use
        s, e = 0, 0         # pointers into the start and end arrays

        while s < len(intervals):
            if start[s] < end[e]:
                # a new meeting starts before the earliest ongoing meeting ends —
                # need an additional room
                s += 1
                count += 1
            else:
                # a meeting has ended before (or when) the next one starts —
                # free up a room
                e += 1
                count -= 1

            res = max(res, count)  # track the peak number of rooms needed at any point in time

        return res

        # Time Complexity:  O(n log n) — dominated by sorting both arrays
        # Space Complexity: O(n) — two separate sorted arrays