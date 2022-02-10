#
#The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
#of rows like this:
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
#


class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1:
            return s

        N = len(s)
        p = 2*(numRows-1)
        out = ''

        for i in range(numRows):

            # First and last rows
            if i == 0 or i == numRows-1:
                out += s[i:N:p]

            else:
                # For interior rows, we need every pth character at two
                # different offsets (i and p-i) interleaved.
                # There might be a more 'pythonic' way to do this interleaving
                m = p-2*i
                for j in range(i, N, p):
                    out += s[j]
                    if j+m < N:
                        out += s[j+m]

        return out
