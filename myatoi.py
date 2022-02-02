# converts a string to a 32 bit integer
# This is stupidly ugly in python. I think it might feel more elegant in C

class Solution:
    def myAtoi(self, s: str) -> int:
    
        LOW = -2147483648
        HIGH = 2147483647
        
        
        i=0
        while i<len(s) and s[i]==' ':
            i+=1
        
        
        if i>=len(s): return 0
            
        neg = (s[i] == '-')
        if s[i] == '-' or s[i]=='+':
            i+=1
            
        while i<len(s) and s[i]=='0':
            i+=1
        
        L = []
        for j in range(i, len(s)):
            o = ord(s[j])
            if o >=48 and o < 58:
                L += [o-48]
            else:
                break
                
        if len(L) > 10:
            if neg:
                return LOW
            else:
                return HIGH
        
        p10 = 1
        T = 0
        for v in reversed(L):
            T += v*p10
            p10 *= 10
        
        if neg: T = -T
            
        if T< LOW: return LOW
        if T> HIGH: return HIGH
        return T
            