class Solution:
    def findMin(self, nums: List[int]) -> int:
        #trivial solution
        minNum = nums[0]

        for i in range(1,len(nums)):
            minNum = min(nums[i], minNum)
        return minNum

