# Input: s = "egg", t = "add"
# Output: true

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_dict = {}
        t_res = []
        for i, j in enumerate(s):
            if j not in s_dict:
                if t[i] not in t_res:
                    s_dict[j] = t[i]
                    t_res.append(t[i])
                else:
                    return False
            else:
                if s_dict[j] != t[i]:
                    return False
        return True
