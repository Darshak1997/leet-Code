class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        eucledian = {}
        for i in range(len(points)):
            distance = (((points[i][1]-0)**2)+(points[i][0]-0)**2)**0.5
            eucledian[i] = distance
        heap = []
        for i in eucledian:
            heapq.heappush(heap, (eucledian[i], i))
        res = []
        for _ in range(K):
            res.append(heapq.heappop(heap)[1])
        out = [points[res[i]] for i in range(len(res))]
        return out
