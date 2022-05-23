class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        left, right, top, bottom = 0, n, 0, n
        count  = 1
        result = [[0]*n for i in range(n)]
        while left < right and top < bottom:
            for i in range(left, right):
                result[top][i] = count
                count+=1
            top+=1
            
            for i in range(top,bottom):
                result[i][right-1] = count
                count+=1
            right-=1
            
            if not(left<right and top< bottom):
                break
            
            for i in range(right-1, left -1, -1):
                result[bottom-1][i] = count
                count+=1
            bottom-=1
            
            for i in range(bottom-1, top-1, -1):
                result[i][left] = count
                count+=1
            left+=1
        return result
        