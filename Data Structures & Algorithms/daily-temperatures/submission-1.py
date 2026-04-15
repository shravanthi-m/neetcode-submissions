class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        out = [0]*len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and t>stack[-1][0]:
                T, ind = stack.pop()
                out[ind] = i-ind
            stack.append([t, i])
        return out