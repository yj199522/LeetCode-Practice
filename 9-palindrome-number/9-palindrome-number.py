class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x is None or x < 0:
            return False
        
        data = str(x)
        
        return data == data[::-1]
        