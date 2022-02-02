<<<<<<< current
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
        
        
            
S = Solution()
=======
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
        
        
            
S = Solution()
print(S.lengthOfLongestSubstring('bab'))
>>>>>>> before discard
