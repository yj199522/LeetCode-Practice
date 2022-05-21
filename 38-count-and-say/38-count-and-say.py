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
#         if n == 1:
#             return '1'
        
#         prev = self.countAndSay(n-1)
#         res = ''
#         count = 1
        
#         for i in range(len(prev)):
#             if i == len(prev) - 1 or prev[i] != prev[i+1]:
#                 res+= str(count) + prev[i]
#                 count = 1
#             else:
#                 count+=1
#         return res