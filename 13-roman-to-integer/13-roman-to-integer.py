class Solution:
    def romanToInt(self, s: str) -> int:
        if s is None:
            return 0
        value = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        i = 0
        while i < len(s):
            if i+1 < len(s) and value[s[i+1]] > value[s[i]]:
                total+= (value[s[i+1]] - value[s[i]])
                i+=2
                continue
            total+= value[s[i]]
            i+=1
        return total