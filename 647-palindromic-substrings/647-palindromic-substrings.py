class Solution:
    def countSubstrings(self, s: str) -> int:
        if s is None or len(s) is 0:
            return 0
        result = 0
        for i in range(len(s)):
            result+=self.helper(s,i,i)
            result+=self.helper(s,i,i+1)
        return result
    
    def helper(self,s,left,right):
        result = 0
        while left>=0 and right < len(s) and s[left] == s[right]:
            result+=1
            left-=1
            right+=1
        return result
        
        