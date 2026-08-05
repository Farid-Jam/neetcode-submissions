class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}
        for c in s:
            if c not in pairs:
                stack.append(c)
            else:
                if len(stack) < 1:
                    return False
                if stack[-1] != pairs[c]:
                    return False
                stack.pop()
        return len(stack) == 0
