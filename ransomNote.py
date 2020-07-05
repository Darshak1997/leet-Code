class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        setNote = set(ransomNote)
        for i in setNote:
            if ransomNote.count(i) > magazine.count(i):
                return False
        return True
        
        # dicNote = {}
        # for i in ransomNote:
        #     if i not in dicNote.keys():
        #         dicNote[i] = 1
        #     else:
        #         dicNote[i] += 1
        # dicMag = {}
        # for i in magazine:
        #     if i not in dicMag.keys():
        #         dicMag[i] = 1
        #     else:
        #         dicMag[i] += 1
        # count = 0
        # for i in dicMag.keys():
        #     if i in dicNote.keys():
        #         if dicMag[i] >= dicNote[i]:
        #             count += 1
        # if count == len(dicNote):
        #     return True
        # return False
        
