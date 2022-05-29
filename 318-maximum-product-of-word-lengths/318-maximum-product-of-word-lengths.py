class Solution:
    def maxProduct(self, words: List[str]) -> int:
        result = 0
        i = 0
        char_set = [set(i) for i in words]
        while i < len(words) - 1:
            j = i + 1
            while j < len(words):
                if not (char_set[i] & char_set[j]):
                    result = max(result, len(words[i]) * len(words[j]))
                j+=1
            i+=1
        return result
                
        