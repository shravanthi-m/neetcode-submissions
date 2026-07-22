class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ct = {}
        frequency = [[] for i in range(len(nums)+1)]
        out = []

        for i in range(len(nums)):
            ct[nums[i]] = 1 + ct.get(nums[i], 0)
        
        for val, freq in ct.items():
            frequency[freq].append(val)
        
        for i in range(len(frequency)-1, 0, -1):
            for val in frequency[i]:
                out.append(val)
                if len(out) == k:
                    return out
        
        