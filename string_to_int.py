class Solution:
    def myAtoi(self, str: str) -> int:
        
        ls = list(str.strip())
        if len(ls) == 0:
            return 0
        MAX_INT = 2**31-1
        MIN_INT = -2**31
        sign = -1 if ls[0] == "-" else 1
        if ls[0] in ['-', '+']:
            del ls[0]
        ret, i = 0, 0
        while i < len(ls) and ls[i].isdigit():
            ret = ret*10 + ord(ls[i]) - ord('0')
            i += 1
        if sign*ret > MAX_INT:
            return MAX_INT
        if sign*ret < MIN_INT:
            return MIN_INT
        return (sign*ret)
