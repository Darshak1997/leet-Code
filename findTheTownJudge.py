class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        count = [0] * (N + 1)
        for i, j in trust:
            count[i] -= 1
            count[j] += 1
        for i in range(1, N+1):
            if count[i] == N-1:
                return i
        return -1
        
        # if trust == [] and N == 1:
        #     return 1
        # incoming = {}
        # setN = set()
        # for i in range(len(trust)):
        #     setN.add(trust[i][0])
        #     if incoming.get(trust[i][1]):
        #         incoming[trust[i][1]] += 1
        #     else:
        #         incoming[trust[i][1]] = 1
        # # print(setN)
        # for i in incoming:
        #     if incoming[i] == N-1 and (i not in setN):
        #         return i
        # return -1
