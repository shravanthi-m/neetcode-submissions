class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # first solution
        # for i in range(0,(len(numbers)-1)):
        #     for j in range(i+1, (len(numbers))):
        #         s = numbers[i] + numbers[j]
        #         if s == target:
        #             return [i+1, j+1]
        #         if s > target:
        #             break
        # optimal solution
        #
        l = 0
        r = len(numbers) - 1
        while l<r:
            s = numbers[l] + numbers[r]
            if s>target:
                r -= 1
            elif s<target:
                l += 1
            else:
                return [l+1, r+1]