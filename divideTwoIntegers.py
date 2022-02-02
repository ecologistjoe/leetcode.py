# Python, of course, already has this as //
# A more fun implementation would be to use a genetic algorithm to guess
# the bitstring of the quotient ;)

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
            
        MIN = -2147483648
        MAX = 2147483647
        
        if divisor == 0: return None        # Maybe should be MAX ? 
        if dividend == 0: return 0
        if divisor == 1:  return dividend
        if divisor == -1: return -dividend if (dividend > MIN) else MAX
        if abs(divisor) > abs(dividend): return 0
        
        quot = 0;                           #holds quotient, the output
        isNegative = (dividend > 0) == (divisor < 0);
        a = abs(dividend);
        b = abs(divisor);
        
        r = a.bit_length() - b.bit_length()     #max power of two s.t. (2^r)*b <= a
        b = b <<r
        
        # Loop over the power-of-two multiples of b that are smaller/equal to a
        # in reverse order. If it can be subtracted out with a remainder, then
        # increment quotient by that power of two and update a to be the remainder
        for i in range(r,-1,-1):  # e.g. R=5:  [5 4 3 2 1 0]
            if a-b >= 0:
                a = a-b
                quot += 1<<i
            b >>= 1
        
        if isNegative:
            quot = -quot
            
        return quot


S = Solution();
print(S.divide(256, -2))