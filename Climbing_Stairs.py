class Solution:
    def climbStairs(self, n: int) -> int:
        self.mapp = {1:1, 2:2}
        return self.decision(n)
        
    def decision(self, n):
        if n not in self.mapp:
            self.mapp[n] = self.decision(n-1) + self.decision(n-2)
        return self.mapp[n]
