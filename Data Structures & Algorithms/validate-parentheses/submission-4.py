class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        partners = {']': '[', ')': '(', '}': '{'}
        for c in s:
            if c in partners:
                if not stack or stack[-1] != partners[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        
        return (len(stack)) == 0