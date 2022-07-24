import bisect
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for m in matrix:
            t=bisect.bisect(m,target)-1
            if t<0:continue
            if m[t]==target:return True
        return False