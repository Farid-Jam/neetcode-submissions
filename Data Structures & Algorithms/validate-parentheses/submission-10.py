class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {'}': '{', ')' : '(', ']' : '['}
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                if len(stack) < 1:
                    return False
                top = stack.pop()
                if top != pair[c]:
                    return False
            
        return len(stack) == 0