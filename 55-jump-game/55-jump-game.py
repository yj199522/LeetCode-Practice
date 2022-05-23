class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if(n == 1):
            return True
        if(n==0): 
            return False
        
        # Go backwards starting at last_index-1
        last_index = n-1
        for i in range(n-2, -1, -1):
            # Distance to last index
            distance = last_index-i
            if( distance <= nums[i]):
                # Current index can reach end
                last_index = i
        
        return last_index == 0