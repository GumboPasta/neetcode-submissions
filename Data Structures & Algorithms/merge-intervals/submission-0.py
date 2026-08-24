class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # Key Data Structure: Interval Merging (Sort + Greedy Scan)

        intervals.sort(key=lambda interval: interval[0])  # sort by start time first
        merged = []

        for interval in intervals:
            # if merged is empty, or the last merged interval ends before
            # this one starts, there's no overlap — just add it as a new entry
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # overlap with the last merged interval — extend its end
                # to cover whichever is further out
                last = merged[-1]
                last[1] = max(last[1], interval[1])

        return merged

        # Time Complexity:  O(n log n) — dominated by the sort
        # Space Complexity: O(n) — merged result list