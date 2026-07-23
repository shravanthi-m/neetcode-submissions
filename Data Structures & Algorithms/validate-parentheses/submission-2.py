class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        startEnd = {'(':')', '[':']', '{':'}'}
        if not s:
            return False
        for i in range(len(s)):
            if s[i] in startEnd.keys():
                stack.append(s[i])
            if s[i] in startEnd.values():
                if not stack:
                    return False
                top = stack.pop()
                if startEnd[top] == s[i]:
                    continue
                return False
        return True if not stack else False