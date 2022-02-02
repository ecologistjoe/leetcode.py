# Find the length of the longest substring in 's' that doesn't have repeating
# characters. Makes use of a python dictionary to store the last time a character
# was encountered in the string.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        D = {}
        cnt = 0
        max_count = 0
        for i,k in enumerate(s):
            
            if k in D:
                cnt = min(cnt+1, i-D[k])
                D[k] = i
            else:
                D[k] = i
                cnt += 1
            
            if cnt > max_count:
                max_count = cnt

        return max_count
        