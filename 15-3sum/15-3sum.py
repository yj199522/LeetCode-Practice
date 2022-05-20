class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if nums is None or len(nums) < 3:
            return []
        
        nums = sorted(nums)
        result = []
        for i in range(0, len(nums) - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = len(nums) - 1
            while(left < right):
                if nums[i] + nums[left] + nums[right] == 0:
                    if [nums[i],nums[left],nums[right]] not in result:
                        result.append([nums[i],nums[left],nums[right]])
                    if left < right and nums[left] == nums[left+1]:
                        left+=1
                    if left < right and nums[right] == nums[right-1]:
                        right-=1
                    left+=1
                    right-=1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -=1
                else:
                    left+=1
        return result
        