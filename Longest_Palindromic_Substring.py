class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        d = {}
        def f(s):
            if s not in d:
                maxL = 0
                for c in set(s):
                    # print(c)
                    i, j = s.find(c), s.rfind(c)
                    # print(i, j)
                    maxL = max(maxL, 1 if i==j else 2+f(s[i+1:j]))
                    # print("maximum", maxL)
                
                d[s] = maxL
                # print(d)
            return d[s]
        
        return f(s)
