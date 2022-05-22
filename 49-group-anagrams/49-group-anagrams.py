class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for i in strs:
            data = ''.join(sorted(i))
            if data not in dic:
                dic[data] = [i]
            else:
                dic[data].append(i)
        result = list(dic.values())
        return result[::-1]
        