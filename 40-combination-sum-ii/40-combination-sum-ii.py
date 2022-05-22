class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res= []
        subSet = []
        length = len(candidates)
        def traverse(pos, add):
            if add == target:
                res.append(subSet.copy())
                return
            if add > target:
                return
            for i in range(pos, length):
                if i > pos and candidates[i - 1] == candidates[i]:
                    continue
                subSet.append(candidates[i])
                add += candidates[i]
                traverse(i + 1, add)
                add -= candidates[i]
                subSet.pop()
        traverse(0, 0)
        return res
        # return arr