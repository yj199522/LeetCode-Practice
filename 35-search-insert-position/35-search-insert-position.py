class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums is None:
            return 0
        for index, item in enumerate(nums):
            if item >= target: return index
        return len(nums)