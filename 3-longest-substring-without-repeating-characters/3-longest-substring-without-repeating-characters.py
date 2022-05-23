class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s is None or len(s) <=1:
            return len(s)
        result = 0
        char = set()
        l = 0
        for r in range(len(s)):
            while s[r] in char:
                char.remove(s[l])
                l+=1
            char.add(s[r])
            result = max(result, r - l + 1)
        return result
        