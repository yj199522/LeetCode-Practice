class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {'2': ['a','b','c'],
                   '3': ['d','e','f'],
                   '4': ['g','h','i'],
                   '5': ['j','k','l'],
                   '6': ['m','n','o'],
                   '7': ['p','q','r', 's'],
                   '8': ['t','u','v'],
                   '9': ['w','x','y', 'z']}
        
        res = []
        stack = []
        
        def dfs(digits):
            if not digits:
                res.append("".join(stack))
                return
            
            for i in mapping[digits[0]]:
                stack.append(i)
                dfs(digits[1:])
                stack.pop()
        
        if digits:
            dfs(digits)
        return res
        