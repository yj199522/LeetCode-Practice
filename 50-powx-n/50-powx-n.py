class Solution:
    def myPow(self, x: float, n: int) -> float:
        newN = n
        if(n < 0):
            newN = abs(n)
            
        result = 1
        while newN != 0:
            if(newN % 2 == 1):
                result = result * x
            x = x * x
            newN = newN // 2
        
        if(n < 0):
            return(1/result)
        return(result)