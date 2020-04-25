class Solution:
    def reformat(self, s: str) -> str:
        if len(s) == 1:
            return s
        
        if s.isalpha() == True:
            return ""
        
        if s.isdigit() == True:
            return ""
        
        
        
        letter = ""
        num = ""
        res = ""
        for i in s:
            if i.isalpha() == True:
                letter += i
            elif i.isdigit() == True:
                num += i
        
        if len(num) > len(letter):
            res = "".join("".join(f for f in tup) for tup in zip(num, letter))
            if len(res) < len(s):
                res += num[len(num)-1]
        if len(num) <= len(letter):
            res = "".join("".join(f for f in tup) for tup in zip(letter, num))
            if len(res) < len(s):
                res += letter[len(letter)-1]
        return(res)
