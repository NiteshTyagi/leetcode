class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = list(zip(indices,s))
        # print(result)
        result.sort()
        s = ''
        for i in result:
            s+=i[1]
        return s
