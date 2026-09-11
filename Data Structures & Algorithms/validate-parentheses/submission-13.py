class Solution:
    def isValid(self, s: str) -> bool:
        partners = {')': '(', '}': '{', ']': '['}
        stack = []
        for c in s:
            if c in partners:
                if not stack or stack[-1] != partners[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        
        return not len(stack)