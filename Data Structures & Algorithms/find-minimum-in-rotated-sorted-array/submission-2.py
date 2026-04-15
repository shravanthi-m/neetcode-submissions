class Solution:
    def findMin(self, nums: List[int]) -> int:
        #binary search solution
        #find the peak in the array 
        s,e = 0, len(nums)-1
        out = nums[0]

        while s<=e:
            if nums[s]<nums[e]:
                out = min(nums[s], out)
                break

            mid = (s+e)//2
            out = min(out, nums[mid])
            if nums[mid]>=nums[s]:
                s = mid+1
            else:
                e = mid-1
        return out

        #trivial solution
        # minNum = nums[0]

        # for i in range(1,len(nums)):
        #     minNum = min(nums[i], minNum)
        # return minNum

