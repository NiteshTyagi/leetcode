class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        r=[]
        row_count = [(index,row.count(1)) for index,row in enumerate(mat)]
        row_count.sort(key=lambda x:x[1])
        for f,s in row_count[:k]:
            r.append(f)
        return r
