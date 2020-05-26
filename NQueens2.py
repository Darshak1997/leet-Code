class Solution:
    def totalNQueens(self, n: int) -> int:
        self.cols = [False]*n
        self.diag1 = [False]*2*n
        self.diag2 = [False]*2*n
        return self.backtrack(0, 0, n)
    
    def backtrack(self, row, count, n):
        for col in range(n):
            d1 = row + col
            d2 = row-col
            if self.cols[col] or self.diag1[d1] or self.diag2[d2]:
                continue
            if row == n-1:
                count += 1
                return count
            else:
                self.cols[col] = self.diag1[d1] = self.diag2[d2] = True
                count = self.backtrack(row+1, count, n)
                self.cols[col] = self.diag1[d1] = self.diag2[d2] = False
        return count
