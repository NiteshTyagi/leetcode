class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        result = [S]
        for i,v in enumerate(S):
            if v.isalpha():
                result.extend([temp[:i]+v.swapcase()+temp[i+1:] for temp in result])
        return result
                    
