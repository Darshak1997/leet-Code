import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq._heapify_max(stones)
        print(stones)
        while len(stones)>1:
            top1 = heapq._heappop_max(stones)
            top2 = heapq._heappop_max(stones)
            print(top1, top2)
            if top1 != top2:
                diff = abs(top2-top1)
                heapq.heappush(stones, diff)
                heapq._heapify_max(stones)
        if stones:
            return(heapq.heappop(stones))
        return 0
        
