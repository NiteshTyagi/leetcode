class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        row = len(isWater)
        col = len(isWater[0])
        queue = [] 
        
        def find_adj(ele):
            r=ele[0]
            c=ele[1]
            return [[r+1,c],[r-1,c],[r,c+1],[r,c-1]]
            
        for r in range(row):
            for c in range(col):
                if isWater[r][c]:
                    isWater[r][c]=0
                    queue.append([r,c])
                else:
                    isWater[r][c]=-1
            
        while queue:
            ele = queue.pop(0)
            current_level = isWater[ele[0]][ele[1]]
            for r,c in find_adj(ele):
                if 0<=r<row and 0<=c<col and isWater[r][c]==-1:
                    isWater[r][c]=current_level+1
                    queue.append([r,c])
​
        return isWater
