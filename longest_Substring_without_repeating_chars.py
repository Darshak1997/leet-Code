class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        max_so_far = curr_max = start = 0
        for i, v in enumerate(s):
            if v in dic and dic[v] >= start:
                max_so_far = max(max_so_far, curr_max)
                curr_max = i - dic[v]
                start = dic[v] + 1
            else:
                curr_max += 1
            dic[v] = i
                
        return max(curr_max, max_so_far)
        
        
        # Brute Force
        # if not s:
        #     return 0
        # length = []
        # for i in range(len(s)):
        #     res = []
        #     for j in range(i, len(s)):
        #         if s[j] not in res:
        #             res.append(s[j])
        #         else:
        #             # length.append(len(res))
        #             break
        #         length.append(len(res))
        # return(max(length))
                
