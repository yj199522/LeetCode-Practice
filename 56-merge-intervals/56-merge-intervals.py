class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if intervals is None:
            return []
        if len(intervals) == 1:
            return intervals
        
        i = 1
        intervals.sort(key = lambda i: i[0])
        result = [intervals[0]]
        for start, end in intervals[1:]:
            if start<= result[-1][1]:
                result[-1][1] =  max(end, result[-1][1])
            else:
                result.append([start, end])
        return result
                