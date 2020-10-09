class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        
        for i in dic.keys():
            if dic[i] == 1:
                return s.index(i)
            
        return -1
