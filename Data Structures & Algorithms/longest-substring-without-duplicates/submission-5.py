class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = deque([])
        maxCount = 0
        count = 0
        p = 0
        while p<len(s):
            print()
            if s[p] in seen:
                while s[p] in seen:
                    seen.popleft()
                    count -= 1
            seen.append(s[p])
            count += 1
            p += 1 
            maxCount = max(maxCount, count)
        return maxCount