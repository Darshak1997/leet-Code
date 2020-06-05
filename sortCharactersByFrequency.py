import heapq
import collections
class Solution:
    def frequencySort(self, s: str) -> str:
        # if len(s) == 0:
        #     return ""
        dic = {}
        for i, v in enumerate(s):
            if v not in dic:
                dic[v] = 1
            else:
                dic[v] += 1
        heap = []
        for i in dic:
            heapq.heappush(heap, (-dic[i], i))
        res = ""
        for _ in range(len(dic)):
            temp = heapq.heappop(heap)
            res += -temp[0]*temp[1]
        return(res)
            
