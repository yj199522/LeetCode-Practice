class Solution:
    def reverse(self, x: int) -> int:
        if x is None or x is 0:
            return x
    
        result = str(x)
        if result[-1] == '0':
            result = result[:len(result)-1]
        result = result[::-1]
        
        if result[-1] == '-':
            result = result[:len(result)-1]
            result = '-' + result
        result = int(result)
        if (2**31 - 1) > result > (2**31 * -1):
            return result
        else:
            return 0