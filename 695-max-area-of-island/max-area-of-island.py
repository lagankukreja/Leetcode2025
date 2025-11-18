class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        area = 0
        visited = set()

        def bfs(i,j):

                if (0<=i<rows and 0<= j< cols) and ((i,j) not in visited and grid[i][j]==1):
                        visited.add((i,j))
                        return 1+ bfs(i+1,j)\
                                + bfs(i-1,j)\
                                + bfs(i,j+1)\
                                + bfs(i,j-1)
                else:
                    return 0
        for i in range(rows):
            for j in range(cols):
                    curr_area = bfs(i,j)
                    area = max(area, curr_area)
        return area