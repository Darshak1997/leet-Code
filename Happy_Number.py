class Solution:
    def isHappy(self, n: int) -> bool:
        res = set()
        while n not in res:
            res.add(n)
            n = sum([int(x) **2 for x in str(n)])
        if n == 1:
            return True
