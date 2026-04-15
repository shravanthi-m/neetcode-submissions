class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ch in tokens:
            if ch == "+":
                exp2 = stack.pop()
                exp1 = stack.pop()
                stack.append(exp1+ exp2)
            elif ch == "-":
                exp2 = stack.pop()
                exp1 = stack.pop()
                stack.append(exp1 - exp2)
            elif ch == "*":
                stack.append(stack.pop()*stack.pop())
            elif ch == "/":
                exp2 = stack.pop()
                exp1 = stack.pop()
                stack.append(int(float(exp1)/exp2))
            else:
                stack.append(int(ch))
        return stack[0]
