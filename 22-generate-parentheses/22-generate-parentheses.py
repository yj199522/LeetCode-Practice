class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ["()"]
        
        ans = []
        comb = []
        
        def dfs(left, right):
            if len(comb) == n*2:
                ans.append("".join(comb))
                return
            
            if left > 0:
                comb.append("(")
                dfs(left - 1, right)
                comb.pop()
                
            if left < right:
                comb.append(")")
                dfs(left, right - 1)
                comb.pop()
                
        dfs(n, n)
        
        return ans
        