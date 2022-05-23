class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        total = max(nums)
        curr_sum = 0
        for i in nums:
            curr_sum+=i
            if curr_sum > total:
                total = curr_sum
            if curr_sum<0:
                curr_sum = 0
        return total
            
        