class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        
        prevData = self.countAndSay(n-1)
        result = ''
        count = 1
        for j in range(len(prevData)):
            if j == len(prevData) - 1 or prevData[j] != prevData[j+1]:
                result+= str(count)+prevData[j]
                count = 1
            else:
                count+=1
        return result
