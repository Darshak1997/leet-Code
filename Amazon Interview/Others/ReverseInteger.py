class Solution:
    def reverse(self, x: int) -> int:
        negate = False
        if x < 0:
            x = abs(x)
            negate = True
        final = 0
        while x>0:
            rem = x%10
            final = (final*10)+rem
            x = x//10
        if final > (2**31)-1 or final < -(2**31):
            return 0
        if negate:
            return -final
        return final
