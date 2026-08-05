class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {c : 0 for c in s}
        l = 0
        r = l
        longest = 0
        curr = 0
        while r < len(s):
            if mp[s[r]] > 0:
                mp[s[l]] -= 1
                l += 1
                curr -= 1
            else:
                mp[s[r]] += 1
                curr += 1
                longest = max(curr, longest)
                r += 1
        return longest
