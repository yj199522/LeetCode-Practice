class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        result = []
        i = 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                nums.pop(i)
                continue
            i+=1
        return len(nums)