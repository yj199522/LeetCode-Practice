class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0 or nums is None:
            return len(nums)
        i = 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                nums.pop(i)
                continue
            i+=1
        return len(nums)