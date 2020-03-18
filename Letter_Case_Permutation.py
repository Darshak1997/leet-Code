class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = [""]
        for char in S:
            l = []
            for i in res:
                # print(">>",i)
                if char.isdigit():
                    l.append("%s%s"%(i,char))
                else:
                    l.append("%s%s"%(i,char.lower()))
                    l.append("%s%s"%(i,char.upper()))
                # print(">",l)
            res = l
        return res
