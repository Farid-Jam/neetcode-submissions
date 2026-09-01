class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        window = [0] * 26
        s = [0] * 26
        for i in range(len(s1)):
            window[ord(s1[i]) - ord('a')] += 1
            s[ord(s2[i]) - ord('a')] += 1
        
        l, r = 0, len(s1)
        while r < len(s2):
            if window == s:
                return True
            
            s[ord(s2[r]) - ord('a')] += 1
            s[ord(s2[l]) - ord('a')] -= 1

            l += 1
            r += 1
        
        return window == s