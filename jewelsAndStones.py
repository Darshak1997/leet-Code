class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        setJ = set(J)
        count = 0
        for i in S:
            if i in setJ:
                count += 1
        return count
        
        
        # count = 0
        # for i in S:
        #     if i in J:
        #         count += 1
        # return count
        
        
        # dic = {}
        # for i in J:
        #     dic[i] = 0
        # count = 0
        # for i in S:
        #     if i in dic.keys():
        #         count += 1
        # return count
