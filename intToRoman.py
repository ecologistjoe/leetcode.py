class Roman:
    def intToRoman(self, num: int) -> str:
        
        symbols = [['','I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'],
                   ['','X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
                   ['','C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
                   ['','M', 'MM', 'MMM']]
        
        roman = ''
        i = 0
        while num > 0:
            d = num % 10
            roman = symbols[i][d] + roman
            num = num//10
            i += 1
        
        return roman
        
    def romanToInt(self, s: str) -> int:
        
        vals = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        
        N = len(s)
        val = 0
        i = 0
        while i < N:
            if i<N-1 and vals[s[i+1]] > vals[s[i]]:
                val += vals[s[i+1]]-vals[s[i]]
                i += 2
            else:
                val += vals[s[i]]
                i += 1
            
        return val