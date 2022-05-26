class Solution:
    def uniquePaths(self, m: int, n: int) -> int:  
        memo = {(0,1):1 , (1,0):1, (1,1):1}
        for row in range(1, m+1):
            for col in range(1, n+1):
                if row == 1:
                    memo[(row,col)] = memo[(row, col-1)]
                elif col == 1:
                    memo[(row, col)] = memo[(row-1, col)]
                else:
                    memo[(row, col)] = memo[(row-1,col)] + memo[(row, col-1)]
        
        return memo[(row, col)]
                
                
        