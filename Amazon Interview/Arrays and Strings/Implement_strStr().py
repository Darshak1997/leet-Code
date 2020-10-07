class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        for i in range(len(haystack) - len(needle) + 1):
            end = i + len(needle)
            if haystack[i:end] == needle:
                return i
            
        return -1
