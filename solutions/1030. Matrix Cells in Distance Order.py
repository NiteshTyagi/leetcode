class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        temp = []
        for i in range(R):
            for j in range(C):
                d = abs(r0-i)+abs(c0-j)
                temp.append(([i,j],d))
        temp.sort(key=lambda x:x[1])
        
        result=[]
        for i in temp:
            result.append(i[0])
        return result
