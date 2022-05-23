class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        total = nums[0]
        curr_sum = 0
        for i in nums:
            if curr_sum<0:
                curr_sum = 0
            curr_sum+=i
            total = max(curr_sum, total)
        return total
            
        