class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # Key Data Structure: Interval Merging (Sort + Greedy Scan)

        intervals.sort(key=lambda interval: interval[0])  # sort by start time —
                                                            # guarantees overlapping intervals end up adjacent
        merged = []

        for interval in intervals:
            # no overlap if merged is empty, or the last merged interval
            # ends before this one even starts
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)  # add as a brand new, separate interval
            else:
                # overlap — rebuild the last merged interval with the
                # same start (already correct due to sorting) and the
                # farthest-reaching end between the two
                merged[-1] = [merged[-1][0], max(merged[-1][1], interval[1])]

        return merged

        # Time Complexity:  O(n log n) — dominated by the sort
        # Space Complexity: O(n) — merged result list