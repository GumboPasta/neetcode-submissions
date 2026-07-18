class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # Key Data Structure: Binary Search on Partition

        # Always binary search on the smaller array for efficiency
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A

        total = len(A) + len(B)
        half = total // 2  # left half must contain exactly this many elements

        l, r = 0, len(A)  # search space is partition positions on A (0 to len(A))

        while True:
            p1 = (l + r) // 2        # partition index on A
            p2 = half - p1            # partition index on B (forced by p1)

            # Max of left side and min of right side for each array
            # Use -inf/+inf as sentinels when partition is at the edge
            maxL1 = A[p1 - 1] if p1 > 0 else float('-inf')
            minR1 = A[p1]     if p1 < len(A) else float('inf')
            maxL2 = B[p2 - 1] if p2 > 0 else float('-inf')
            minR2 = B[p2]     if p2 < len(B) else float('inf')

            if maxL1 <= minR2 and maxL2 <= minR1:
                # Valid partition — max of left half <= min of right half
                if total % 2 == 1:
                    # Odd total: median is the smallest element on the right
                    return min(minR1, minR2)
                else:
                    # Even total: median is average of middle two elements
                    return (max(maxL1, maxL2) + min(minR1, minR2)) / 2

            elif maxL1 > minR2:
                # Left side of A is too big — move partition left
                r = p1 - 1
            else:
                # Left side of B is too big — move partition right on A
                l = p1 + 1

        # Time Complexity: O(log(min(m, n))) — binary search on the smaller array
        # Space Complexity: O(1) — just pointers and sentinel values