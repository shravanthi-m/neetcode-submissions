class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #row binary search
        rs, re = 0, len(matrix)-1
        while rs<=re:
            r = (rs+re)//2
            if target > matrix[r][-1]:
                rs = r+1
            elif target < matrix[r][0]:
                re = r-1
            else:
                break
        
        if not rs<=re:
            return False
        #within row binary search
        s, e = 0, len(matrix[0])
        while s<=e:
            mid = (s+e)//2
            if target>matrix[r][mid]:
                s = mid+1
            elif target<matrix[r][mid]:
                e = mid-1
            else:
                return True
        return False
