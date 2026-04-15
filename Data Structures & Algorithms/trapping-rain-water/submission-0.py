class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        maxL = height[l]
        maxR = height[r]
        out = 0
        if not height:
            return 0

        while l<r:
            if maxL<=maxR:
                l+=1
                # if i>0:
                    # h = min(height[i+1], height[i-1])
                # else:
                    # h = height[i+1]
                maxL = max(maxL, height[l])
                out += maxL-height[l]
                
            else:
                r -= 1
                maxR = max(maxR, height[r])
                out += maxR-height[r]
                
        return out
