class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        res = []
        for i in nums:
            product = product * i
        for i in range(len(nums)):
            if nums[i] == 0:
                product_ = 1
                for j in range(len(nums)):
                    if j != i:
                        product_ = product_ * nums[j]
                res.append(product_)
            else:
                res.append((product//nums[i]))
        return res
        