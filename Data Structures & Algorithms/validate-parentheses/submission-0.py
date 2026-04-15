class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        endbeg = {')':'(', ']':'[', '}':'{'}

        for ch in s:
            if ch in endbeg:
                if stack and stack[-1]==endbeg[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)

        return True if not stack else False