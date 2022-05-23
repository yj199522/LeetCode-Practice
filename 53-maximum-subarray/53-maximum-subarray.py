class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        total = nums[0]
        curr_sum = 0
        for i in nums:
            if curr_sum<0:
                curr_sum = 0
            curr_sum+=i
            if curr_sum > total:
                total = curr_sum
        return total
            
        