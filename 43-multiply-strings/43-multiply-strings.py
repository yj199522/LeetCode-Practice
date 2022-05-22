class Solution:
    def multiply(self, nums1: str, nums2: str) -> str:
        if '0' in [nums1, nums2]:
            return '0'
        
        result = [0] * (len(nums1) + len(nums2))
        
        nums1, nums2 = nums1[::-1], nums2[::-1]
        
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                mutiple = int(nums1[i]) * int(nums2[j])
                result[i+j] += mutiple
                result[i+j+1] += (result[i+j] // 10)
                result[i+j] = (result[i+j] % 10)
        result, beg = result[::-1], 0
        while beg < len(result) and result[beg] == 0:
            beg+=1
        data = map(str, result[beg:])
        return ''.join(data)
        