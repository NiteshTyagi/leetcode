class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        result = 0
        boxTypes.sort(reverse=True,key=lambda x:x[1])
        for nb,nu in boxTypes:
            if truckSize>=nb:
                result+=(nb*nu)
                truckSize-=nb
            else:
                result+=(truckSize*nu)
                truckSize = 0
                break
        return result
