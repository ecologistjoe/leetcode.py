class Solution:
    def reverse(self, x: int) -> int:
                    
        #MIN = -2147483648
        #MAX = 2147483647
        
        
        isneg = x < 0
        x = abs(x)
        
        y = 0
        while x > 0:
            
            a = x % 10
            x = x//10
            
            
            if y > 214748364: return 0
            if y == 214748364:
                if isneg:
                    if a > 7: return 0
                else:
                    if a > 6: return 0
                
            y = 10*y+a
        
        
        if isneg: y = -y
        
        return y