#Given a string s, return the longest palindromic substring in s.
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        longest = 1
        substr = s[0]
        N = len(s)
        
        # Walk through string and check around each character for matching values
        for i in range(1,N):
            
            # Check odd
            p = min(i, N-i-1)
            j = 1
            while j <= p and s[i-j] == s[i+j]:
                j+=1
            if 2*j-1 > longest:
                substr = s[i-j+1:i+j]
                longest = len(substr)
                
            # Check even
            p = min(i, N-i)
            j = 1
            while j <= p and s[i-j] == s[i+j-1]:
                j+=1
            if 2*j-2 > longest:
                substr = s[i-j+1:i+j-1]
                longest = len(substr)
            
                    
        return substr