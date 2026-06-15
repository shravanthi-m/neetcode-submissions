class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        out = []
        l, r = 0, k-1
        while r<len(nums):
            if r!=(len(nums)-1):
                out.append(max(nums[l:r+1]))
            else:
                out.append(max(nums[l:]))
            l += 1
            r += 1
        return out