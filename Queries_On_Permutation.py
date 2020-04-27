class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        p = []
        inc = 0
        index = []
        for inc in range(1, m+1):
            p.append(inc)
        for i in (queries):
            z = p.index(i)
            index.append(z)
            y = p.pop(z)
            p.insert(0, y)
        return index
