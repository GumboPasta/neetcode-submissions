class Solution:
    def longestPalindrome(self, s: str) -> str:

        # Key Data Structure: Two Pointers (Expand Around Center)

        res = ""       # tracks the longest palindrome substring found so far
        resLen = 0     # tracks its length (avoids recalculating len(res) repeatedly)

        for i in range(len(s)):

            # odd length palindromes — center is a single character at i (e.g. "aba")
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # every time the window is valid, check if it's the longest seen so far
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1  # expand outward on both sides simultaneously
                r += 1

            # even length palindromes — center is the gap between i and i+1 (e.g. "abba")
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1

        return res  # longest palindromic substring found across all centers

        # Time Complexity:  O(n^2) — n possible centers (2n-1 total counting odd+even),
        #                   each expansion can take up to O(n) in the worst case
        # Space Complexity: O(1) — only tracking a few pointers and the result string,
        #                   no extra data structures that scale with input size