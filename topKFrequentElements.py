import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i, v in enumerate(nums):
            if v not in dic:
                dic[v] = 1
            else:
                dic[v] += 1
        res = heapq.nlargest(k, dic.keys(), key=dic.get)
        return(res)
            
