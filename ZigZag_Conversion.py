class Solution:
    def convert(self, s: str, numRows: int) -> str:
        line = 0
        pl = 1
        out = [""]*numRows
        for i in range(len(s)):
            out[line] += s[i]
            if numRows > 1:
                line += pl
                if line == 0 or line == numRows-1:
                    pl*= -1
        outStr = ""
        for j in range(numRows):
            outStr += out[j]
        return outStr
