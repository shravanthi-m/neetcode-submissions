class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        out = []
        for i in range(len(temperatures)):
            ct = 0
            higher = False
            j = i+1
            while j<len(temperatures):
                ct +=1
                if temperatures[j]>temperatures[i]:
                    out.append(ct)
                    higher = True
                    break
                j += 1
            if higher == False:
                out.append(0)
        return out
            