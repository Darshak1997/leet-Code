class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.grid = board
        
        # To see if there is a "O" on the boundary
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if i == 0 or j == 0 or i == len(self.grid)-1 or j == len(self.grid[0])-1:
                    if self.grid[i][j] == "O":
                        self.no_boundary(i, j)
        
        # To check if there are regions to be flipped
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == "O":
                    self.boundary(i, j)
                    
        # To replace surrounded region by "O"
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == "#":
                    self.grid[i][j] = "O"
        
    # To mark the connected "O"s from boundary
    def no_boundary(self, i, j):
        if i < 0 or i >= len(self.grid) or j < 0 or j >= len(self.grid[0]) or self.grid[i][j] != "O":
            return
        
        self.grid[i][j] = "#"
        self.no_boundary(i-1, j)
        self.no_boundary(i+1, j)
        self.no_boundary(i, j-1)
        self.no_boundary(i, j+1)
        
    # To check if a "O" can be flipped
    def boundary(self, i, j):
        if i < 0 or i >= len(self.grid) or j < 0 or j >= len(self.grid[0]) or self.grid[i][j] != "O":
            return
        
        self.grid[i][j] = "X"
        self.boundary(i-1, j)
        self.boundary(i+1, j)
        self.boundary(i, j-1)
        self.boundary(i, j+1)
