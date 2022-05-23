class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s is None or len(s) == 0:
            return 0
        
        s = s.split(' ')
        
        n = len(s) - 1
        
        while n!=0:
            if s[n] == '':
                s.pop()
            else:
                break
            n-=1
        
        return len(s[-1])
        