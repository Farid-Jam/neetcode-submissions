class Solution:
    def isValid(self, s: str) -> bool:
        partners = {')': '(', '}': '{', ']': '['}
        stack = []
        for c in s:
            if c not in partners:
                stack.append(c)
            else:
                if not stack or stack[-1] != partners[c]:
                    return False
                stack.pop()
        return len(stack) == 0