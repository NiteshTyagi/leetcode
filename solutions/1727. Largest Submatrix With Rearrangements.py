class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        n_r, n_c, res = len(matrix), len(matrix[0]), 0
​
        for r in range(1, n_r):
            for c in range(n_c):
                matrix[r][c] += matrix[r-1][c] if matrix[r][c] else 0
​
        for r in range(n_r): 
            matrix[r].sort(reverse = True)
            for c in range(n_c):
                res = max(res, (c+1)*matrix[r][c])
                
        return res
                
