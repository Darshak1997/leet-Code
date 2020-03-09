class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur_string = ""
        cur_Num = 0
        for c in s:
            if c=="[":
                stack.append(cur_string)
                stack.append(cur_Num)
                cur_string = ""
                cur_Num = 0
            elif c=="]":
                num = stack.pop()
                prev_string = stack.pop()
                cur_string = prev_string+num*cur_string
            elif c.isdigit():
                cur_Num = cur_Num*10 + int(c)
            else:
                cur_string += c
        return cur_string
