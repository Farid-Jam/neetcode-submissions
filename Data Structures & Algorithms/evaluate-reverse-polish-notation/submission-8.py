class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(str(a + b))
            elif token == '-':
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(str(a - b))
            elif token == '/':
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(str(int(a / b)))
            elif token == '*':
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(str(a * b))
            else:
                stack.append(token)
        return int(stack[-1])