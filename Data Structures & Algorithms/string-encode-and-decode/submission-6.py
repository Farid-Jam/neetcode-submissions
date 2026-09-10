class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.extend([str(len(s)), "#", s])
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded = []
        l = r = 0
        while r < len(s):
            if s[r] == "#":
                length = int(s[l:r])
                l = r + 1
                r = l + length
                decoded.append(s[l:r])
                l = r 
            else:
                r += 1
        return decoded