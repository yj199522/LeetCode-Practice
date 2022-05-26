class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sums = 0
        for i in digits:
            sums = sums*10+i
        sums+=1
        return [c for c in str(sums)]
        