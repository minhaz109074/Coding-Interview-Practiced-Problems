class Solution:
    def dfs(self, grid, u, v):
        if u<0 or v<0 or u>= len(grid) or v>= len(grid[0]) or grid[u][v] == 2 or grid[u][v] == 0: return
        
        if grid[u][v] == 1: self.area += 1
        grid[u][v] = 2
        self.dfs(grid, u+1, v)
        self.dfs(grid, u-1, v)
        self.dfs(grid, u, v+1)
        self.dfs(grid, u, v-1)
        
        
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.maxarea = 0
        for u in range(len(grid)):
            for v in range(len(grid[0])):
                 if grid[u][v] == 1 :
                        self.area = 0
                        self.dfs(grid, u, v)
                        self.maxarea = max(self.maxarea, self.area)
                          
        return self.maxarea
        