class TimeMap:

    # Key Data Structures: Binary Search and Hash Map

    def __init__(self):
        self.keyStore = {}  # key → list of [value, timestamp] in ascending timestamp order

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        # timestamps always increase, so appending keeps the list sorted
        self.keyStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.keyStore.get(key, [])  # returns [] safely if key doesn't exist

        l, r = 0, len(values) - 1

        while l <= r:  # <= because the last remaining element still needs to be checked
            m = (l + r) // 2

            if values[m][1] <= timestamp:
                res = values[m][0]  # valid candidate — record it and search right for something closer
                l = m + 1
            else:
                r = m - 1           # timestamp too late, discard right half

        return res  # best value with timestamp <= target, or "" if none exists

    # Time Complexity:
    #   set: O(1) — append to list
    #   get: O(log n) — binary search over n entries for that key
    # Space Complexity: O(n) — storing all n set() entries across the hash map