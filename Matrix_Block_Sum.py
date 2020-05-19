import numpy as np
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        mat2 = np.array(mat)
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                LCi, UCi = max(0, i-K), min(m, i+K)
                LCj, UCj = max(0, j-K), min(m, j+K)
                mat[i][j] = np.sum(mat2[LCi:UCi+1, LCj:UCj+1])
        return mat
    #     row, col = len(mat), len(mat[0])
    #     res = [[0] * col for _ in range(row)] 
    #     r = c = 0
    #     for r in range(row):
    #         for c in range(col):
    #             total = self.rec(r, c, row, col, mat, res, K)
    #             res[r][c] = total
    #     return res
    # def rec(self, r, c, row, col, mat, res, K):
    #     total = 0
    #     for i in range(row):
    #         if i - K <= r <= i + K:
    #             for j in range(col):
    #                 if j - K <= c <= j + K:
    #                     total += mat[i][j]
    #     return total
                        
