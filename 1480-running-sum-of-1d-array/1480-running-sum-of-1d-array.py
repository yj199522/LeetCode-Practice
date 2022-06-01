class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = [nums[0]]
        for i in range(1,len(nums)):
            result.append(sum(nums[:i+1]))
        return result