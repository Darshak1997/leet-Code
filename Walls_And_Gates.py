class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]:
            return
        row, col, inf = len(rooms), len(rooms[0]), 2147483647
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        queue = []
        for i in range(row):
            for j in range(col):
                if rooms[i][j] == 0:
                    queue.append((i, j))
        step = 0
        while queue:
            new_queue = []
            step += 1
            for (x, y) in queue:
                for d in directions:
                    nx, ny = x+d[0], y+d[1]
                    if 0<=nx<row and 0<=ny<col and rooms[nx][ny] == inf:
                        rooms[nx][ny] = step
                        new_queue.append((nx, ny))
            queue = new_queue
