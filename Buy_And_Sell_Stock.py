class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == []:
            return 0
        buy = prices[0] 
        res = 0
        for i in range(1, len(prices)):
            diff = prices[i]-buy
            if diff > res:
                res = diff
            if buy > prices[i]:
                buy = prices[i]
        return res
    
#         if len(prices) == 0:
#             return 0
#         low = float("inf")
#         profit = 0
#         for price in prices:
#             if price > low:
#                 if price - low > profit:
#                     profit = price - low
#             elif price < low:
#                 low = price
                    
#         return profit
