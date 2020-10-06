class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mapping = {}
        start = 0
        maxLen = 0
        
        for i, value in enumerate(s):
            if value in mapping:
                sums = mapping[value] + 1
                if sums > start:
                    start = sums
            num = i - start + 1
            if num > maxLen:
                maxLen = num
            mapping[value] = i
            
        return maxLen
        
#         res = []
#         for i in range(len(s)):
#             currStr = ""
#             start = i
#             while start < len(s) and s[start] not in currStr:
#                 currStr += s[start]
#                 start += 1
#             res.append(len(currStr))
            
#         if not res:
#             return 0
#         return max(res)
