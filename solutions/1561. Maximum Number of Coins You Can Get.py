class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        result = 0
        piles.sort()
        for i in range(1,len(piles)//3+1):
            index = -2*i
            result+= piles[index]
        return result
        
