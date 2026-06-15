class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prod = max(nums)
        currMin, currMax = 1, 1

        for n in nums:
            if n==0:
                currMin, currMax = 1, 1
                continue
            t = currMax*n
            currMax = max(currMax*n, currMin*n, n)
            currMin = min(t, currMin*n, n)
            prod = max(prod, currMax)

        return prod
            