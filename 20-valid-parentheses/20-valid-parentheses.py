class Solution:
    def isValid(self, s: str) -> bool:
        openBrak = ['(', '{', '[']
        closeBrak = [')', '}', ']']
        
        if s is None or s[0] in closeBrak:
            return False
        
        i = 0
        check = []
        while i < len(s):
            if s[i] in openBrak:
                check.append(s[i])
            elif s[i] in closeBrak:
                if len(check) == 0:
                    return False
                checkBrackIndex = openBrak.index(check[-1])
                closeBrackIndex = closeBrak.index(s[i])
                if closeBrackIndex != checkBrackIndex:
                    return False
                check.pop()
            i+=1
        if len(check) == 0:
            return True
        return False
        
        