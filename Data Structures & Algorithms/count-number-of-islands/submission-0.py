class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(row, col):
            if len(grid) <= row or row < 0 or col >= len(grid[0]) or col < 0 or grid[row][col] == "0":
                return 0

            grid[row][col] = "0"
            
            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col-1)
            dfs(row, col+1)

            return 1

        numIslands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                numIslands += dfs(i, j)

        return numIslands