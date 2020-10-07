class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # strs.sort()
        res = []
        dic = {}
        for i in range(len(strs)):
            ls = "".join(sorted(strs[i]))
            if ls not in dic.keys():
                dic[ls] = len(res)
                res.append([strs[i]])
            else:
                pos = dic[ls]
                res[pos].append(strs[i])
        return res
        
