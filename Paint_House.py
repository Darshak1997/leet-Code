class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        def paint_cost(n, color):
            if (n,color) in self.memo:
                return self.memo[(n, color)]
            total = costs[n][color]
            if n == len(costs) - 1:
                pass
            elif color == 0:
                total += min(paint_cost(n+1, 1), paint_cost(n+1, 2))
            elif color == 1:
                total += min(paint_cost(n+1, 0), paint_cost(n+1, 2))
            elif color == 2:
                total += min(paint_cost(n+1, 0), paint_cost(n+1, 1))
            self.memo[(n, color)] = total
            return total
        
        if costs == []:
            return 0
        self.memo = {}
        return min(paint_cost(0,0), paint_cost(0,1), paint_cost(0,2))
