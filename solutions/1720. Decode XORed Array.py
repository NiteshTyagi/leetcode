class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        result = [first]
        for i in encoded:
            xor = result[-1]^i
            result.append(xor)
        return result
        
