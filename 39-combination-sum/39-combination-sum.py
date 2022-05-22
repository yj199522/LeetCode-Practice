class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if candidates is None or len(candidates) == 0:
            return []
        arr = []
        def helper(index, value, path):
            if index == len(candidates):
                if value == 0:
                    arr.append(path[:])
                return
            if candidates[index] <= value:
                path.append(candidates[index])
                helper(index, value-candidates[index],path)
                path.pop()
            helper(index+1,value,path)
        helper(0,target,[])
        return arr
                