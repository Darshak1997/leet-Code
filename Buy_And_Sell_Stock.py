class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        low = float("inf")
        profit = 0
        for price in prices:
            if price > low:
                if price - low > profit:
                    profit = price - low
            elif price < low:
                low = price
                    
        return profit
