class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        minPrice = prices[0]

        for sellP in prices:
            maxProf = max(maxProf, sellP-minPrice)
            minPrice = min(minPrice, sellP)
        
        return maxProf