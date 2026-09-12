class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = defaultdict(int)
        res = 0
        l = 0

        for r in range(len(s)):
            count[s[r]] += 1

            while count[s[r]] == 2:
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        
        return res