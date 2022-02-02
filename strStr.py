# Find the needle in the haystack (substring in string).

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if len(needle) == 0: return 0
        if len(needle) > len(haystack): return -1
        if haystack==needle: return 0
        
        N = len(needle)
        for i in range(len(haystack)-N+1):
            if haystack[i:i+N] == needle:
                return i
        return -1