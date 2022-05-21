class Solution:
    def isValid(self, s: str) -> bool:
        openBrak = ['(', '{', '[']
        closeBrak = [')', '}', ']']
        bracket = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        
        if s is None or s[0] not in bracket:
            return False
        
        i = 0
        check = []
        while i < len(s):
            if s[i] in bracket:
                check.append(bracket[s[i]])
            # elif s[i] in closeBrak:
            #     if len(check) == 0:
            #         return False
            #     checkBrackIndex = openBrak.index(check[-1])
            #     closeBrackIndex = closeBrak.index(s[i])
            #     if closeBrackIndex != checkBrackIndex:
            #         return False
            #     check.pop()
            else:
                if len(check)==0 or s[i]!=check[-1]:
                    return False
                check.pop();
            i+=1
        if len(check) == 0:
            return True
        return False
        
        