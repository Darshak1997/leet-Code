class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        def helper(timestamp):
            to_be_continued = False
            for r in range(row):
                for c in range(col):
                    if grid[r][c] == timestamp:
                        for d in directions:
                            n_row, n_col = r + d[0], c + d[1]
                            if row > n_row >= 0 and col > n_col >= 0:
                                if grid[n_row][n_col] == 1:
                                    grid[n_row][n_col] = timestamp+1
                                    to_be_continued = True
            return to_be_continued
        
        timestamp = 2
        while helper(timestamp):
            timestamp += 1
        
        for r in grid:
            for cell in r:
                if cell == 1:
                    return -1
        return timestamp-2
