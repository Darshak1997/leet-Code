class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        max_value = 2147483647
        if not rooms:
            return
        q = deque()
        
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    q.append((i,j))
        
        while q:
            row, col = q.popleft()
            dist = rooms[row][col]+1
            for dx, dy in (-1,0),(0,1),(0,-1),(1,0):
                r = dy+row
                c = dx+col
                if (r >= 0 and r < len(rooms)) and (c >= 0 and c < len(rooms[0])) and (rooms[r][c] == max_value):
                    rooms[r][c] = dist
                    q.append((r,c))
