def searchLeft(nums, target):
    def condition(mid):
        midValue = nums[mid]
        if midValue == target:
            if mid > 0 and nums[mid-1] == target:
                return 'left'
            else:
                return 'found'
        elif midValue < target:
            return 'right'
        else:
            return 'left'
    return binarySearch(0, len(nums)-1, condition)

def searchRight(nums, target):
    def condition(mid):
        midValue = nums[mid]
        if midValue == target:
            if mid < len(nums) - 1 and nums[mid+1] == target:
                return 'right'
            else:
                return 'found'
        elif midValue < target:
            return 'right'
        else:
            return 'left'
    return binarySearch(0, len(nums)-1, condition)

def binarySearch(left, right, condition):
    while(left <= right):
        mid = (left+right)//2
        conditions = condition(mid)
        if conditions == 'found':
            return mid
        elif conditions == 'right':
            left = mid + 1
        else:
            right = mid - 1
    return -1
        
        
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [searchLeft(nums, target), searchRight(nums, target)]
    