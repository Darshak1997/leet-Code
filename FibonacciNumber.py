class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        if N == (1 or 2):
            return 1
        res = [0]*(N)
        res[0] = 1
        res[1] = 1
        for i in range(2, N):
            res[i] = res[i-1] + res[i-2]
        return res[N-1]
