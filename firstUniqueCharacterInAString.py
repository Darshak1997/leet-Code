class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        setS = set()
        for i, v in enumerate(s):
            if v not in setS:
                d[v] = i
                setS.add(v)
            elif v in d:
                del d[v]
        return min(d.values()) if d else -1
        
        # for i, v in enumerate(s):
        #     if s.count(v) == 1:
        #         return i
        # return -1
