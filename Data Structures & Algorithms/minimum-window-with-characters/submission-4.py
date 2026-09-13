class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        count = Counter(t)
        window = Counter()

        need = len(count)
        have = 0

        res = [-1, -1]
        l = 0

        for r in range(len(s)):
            window[s[r]] += 1

            if window[s[r]] == count[s[r]]:
                have += 1
            
            while have == need and window[s[l]] - 1 >= count[s[l]]:
                window[s[l]] -= 1
                l += 1
            
            if have == need:
                if res == [-1, -1]:
                    res = [l, r]
                else:
                    res = [l, r] if res[1] - res[0] > r - l else res
        
        return s[res[0]: res[1] + 1]
