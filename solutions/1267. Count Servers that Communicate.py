class Solution:
    def __init__(self):
        self.countServer = 0
        
    def mark_flag(self,grid,option=False):
        for g in grid:
            
            flag = 0
            if option:
                flag = g.count('f')
                
            if flag+g.count(1) >1:
                for i in range(len(g)):
                    if g[i]==1:
                        g[i]= 'f'
                        self.countServer+=1     
        return grid
    
    
    def countServers(self, grid: List[List[int]]) -> int:
        grid = self.mark_flag(grid)    
        
        
        colGrid = [[grid[col][row] for col in range(len(grid))] for row in range(len(grid[0]))]
        
        grid = self.mark_flag(colGrid,option=True)
    
        return self.countServer
