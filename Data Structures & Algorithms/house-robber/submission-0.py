class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1]*len(nums)
        def dfs(ind):
            if ind>=len(nums):
                return 0
            if memo[ind] != -1:
                return memo[ind]
            memo[ind] = max(dfs(ind+1), nums[ind]+dfs(ind+2))
            return memo[ind]
        return max(dfs(0), dfs(1))
                
