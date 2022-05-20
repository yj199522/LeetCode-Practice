class Solution:
    def dfs(self, start, end):
        total = 0

        if start > end:
            return 1

        for i in range(start, end+1):
            left = self.dfs(start,i-1)
            right = self.dfs(i+1,end)
            total += left*right

        return total

    def numTrees(self, n):
        return self.dfs(1,n)