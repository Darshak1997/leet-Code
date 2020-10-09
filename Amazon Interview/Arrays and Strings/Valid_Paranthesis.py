class Solution:
    def isValid(self, s: str) -> bool:
        dic = {")": "(", "}": "{", "]": "["}
        closed = []
        for i in s:
            if i in dic:
                topElement = closed.pop() if closed else "#"
                if dic[i] != topElement:
                    return False
            else:
                closed.append(i)
                
        return not closed
