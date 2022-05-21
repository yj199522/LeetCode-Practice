class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        if len(nums) == 4 and sum(nums) == target:
            return [nums]
        result = []
        nums = sorted(nums)
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            while j <= len(nums) - 3:
                left = j + 1
                right = len(nums) - 1
                while(left < right):
                    sums = nums[i] + nums[j] + nums[left] + nums[right]
                    if sums == target:
                        if [nums[i] , nums[j] , nums[left] , nums[right]] not in result:
                            result.append([nums[i] , nums[j] , nums[left] , nums[right]])
                        left+=1
                        right-=1
                    elif sums > target:
                        right-=1
                    else:
                        left+=1
                j+=1
                if j > i + 1 and nums[j] == nums[j-1]:
                    j+=1
        return result