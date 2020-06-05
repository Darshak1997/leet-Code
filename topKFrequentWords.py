import heapq
import collections
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic = {}
        for i, v in enumerate(words):
            if v not in dic:
                dic[v] = 1
            else:
                dic[v] += 1
        heap = []
        for i in dic:
            heapq.heappush(heap, (-dic[i], i))
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return(res)
