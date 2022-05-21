class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) < 3:
            return 0
        result = 10**23
        nums = sorted(nums)
        for i in range(len(nums)-2):
            left = i + 1
            right = len(nums) - 1
            while(left<right):
                sums = nums[i] + nums[left] + nums[right]
                nearest=abs(target - sums)
                if nearest <= abs(target - result) or result is 10**23:
                    result = sums
                    if result < target:
                        left+=1
                    else:
                        right-=1
                elif sums > result:
                    right-=1
                else:
                    left+=1
        return result
        