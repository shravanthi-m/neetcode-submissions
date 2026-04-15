class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(0,(len(numbers)-1)):
            for j in range(i+1, (len(numbers))):
                s = numbers[i] + numbers[j]
                if s == target:
                    return [i+1, j+1]