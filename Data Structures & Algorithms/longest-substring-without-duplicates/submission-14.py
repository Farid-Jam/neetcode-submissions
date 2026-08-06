class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastSeen = {}
        longest = 0
        l, r = 0, 0
        while r < len(s):
            if s[r] in lastSeen:
                l = max(l, lastSeen[s[r]] + 1)
            lastSeen[s[r]] = r
            longest = max(longest, r - l + 1)
            r += 1
        return longest
