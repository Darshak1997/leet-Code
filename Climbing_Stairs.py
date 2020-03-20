class Solution:
    def climbStairs(self, n: int) -> int:
        a = b = 1
        for _ in range(n-1):
            temp = a+b
            a=b
            b=temp
        return b
