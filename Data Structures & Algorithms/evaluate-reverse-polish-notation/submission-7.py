class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                second = int(stack.pop())
                first = int(stack.pop())
                stack.append(first + second)
            elif token == '-':
                second = int(stack.pop())
                first = int(stack.pop())
                stack.append(first - second)
            elif token == '*':
                second = int(stack.pop())
                first = int(stack.pop())
                stack.append(first * second)
            elif token == '/':
                second = int(stack.pop())
                first = int(stack.pop())
                stack.append(int(first / second))
            else:
                stack.append(token)
        return int(stack.pop())