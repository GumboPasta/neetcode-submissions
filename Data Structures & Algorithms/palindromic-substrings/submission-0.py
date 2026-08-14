class Solution:
    def countSubstrings(self, s: str) -> int:

        # Key Data Structure: Two Pointers (Expand Around Center)

        res = 0  # running total of all palindromic substrings found

        for i in range(len(s)):
            res += self.countPali(s, i, i)       # count odd-length palindromes centered at i
            res += self.countPali(s, i, i + 1)    # count even-length palindromes centered between i and i+1

        return res

        # Time Complexity:  O(n^2) — n centers, each expansion takes up to O(n)
        # Space Complexity: O(1) — no extra data structures

    def countPali(self, s, l, r):
        res = 0  # counts every valid palindrome found while expanding from this center

        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1   # every successful expansion IS a new palindrome (not just the biggest one)
            l -= 1
            r += 1

        return res