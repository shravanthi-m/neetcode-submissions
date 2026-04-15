class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l+r)//2
            hours = 0
            for p in piles:
                hours += math.ceil(p/k)
            
            if hours <= h:
                res = min(res,k)
                r = k-1
            else:
                l = k+1
        
        return res


        
        
        #prev sol
        #h- hours to eat, piles-array
        #output-k- min. per hour
        #binary search
        # def timeTaken(val):
        #     res = [math.ceil(x/val) for x in piles]
        #     return sum(res)

        # vals = list(range(1, max(piles)+1))
        # s, e = 0, len(vals)-1
        # curr = float('inf')
        # while s<=e:
        #     m = (s+e)//2
        #     m_val = vals[m]
        #     print(m_val)
        #     if timeTaken(m_val)<=h:
        #         curr = min(curr, m_val)
        #         e = m-1
        #     else:
        #         s = m+1
        # return curr