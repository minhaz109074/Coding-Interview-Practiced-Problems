class Solution:
    def dfs(self, grid, u, v):
        if u<0 or v<0 or u>= len(grid) or v>= len(grid[0]) or grid[u][v] == "#" or grid[u][v] == "0": return
    
        grid[u][v] = "#"
        self.dfs(grid, u+1, v)
        self.dfs(grid, u-1, v)
        self.dfs(grid, u, v+1)
        self.dfs(grid, u, v-1)
        
        
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for u in range(len(grid)):
            for v in range(len(grid[0])):
                 if grid[u][v] == "1" :
                        self.dfs(grid, u, v)
                        count += 1
                        
        return count 
            
             
            
                    
                       
                       
                       
                       