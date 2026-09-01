class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        window = {}
        for i in range(len(t)):
            window[t[i]] = 1 + window.get(t[i], 0)
        
        has = 0
        needs = len(window)
        l = 0
        res = [-1, -1]
        count = {}
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            if s[r] in window and count[s[r]] == window[s[r]]:
                has += 1
            while has == needs:
                if res == [-1, -1] or r - l < res[1] - res[0]:
                    res = [l, r]
                if s[l] in window and count[s[l]] == window[s[l]]:
                    has -= 1
                count[s[l]] -= 1
                l += 1

        if res == [-1, -1]:
            return ""
        
        return s[res[0] : res[1] + 1]