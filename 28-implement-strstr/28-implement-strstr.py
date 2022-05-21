class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack is None or needle is None: 
            return -1
        return -1 if haystack.find(needle) is -1 else haystack.index(needle)
        