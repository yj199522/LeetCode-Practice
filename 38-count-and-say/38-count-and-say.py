class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        
        result = '1'
        
        for i in range(1, n):
            count = 1
            data = '' 
            for j in range(len(result)):
                if j == len(result) - 1 or result[j] != result[j+1]:
                    data+= str(count)+result[j]
                    count = 1
                else:
                    count+=1
            result = data
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