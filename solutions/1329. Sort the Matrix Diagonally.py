class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        col= len(mat[0])
        row = len(mat)
        result = [[None for j in range(col)] for i in range(row)]
​
​
        for i in range(col):
            c=i
            r=0
            flag=True
            R=r
            temp = []
            count=0
            C=c
            while r<row and c<col:
                while flag and R<row and C<col:
                    temp.append(mat[R][C])
                    R+=1
                    C+=1
                if flag:
                    temp.sort()
                    flag=False
                result[r][c] = temp[count]
                count+=1
                r+=1
                c+=1
​
        for i in range(1,row):
            c=0
            r=i
            flag=True
            R=r
            temp = []
            count=0
            C=c
            while r<row and c<col:
                while flag and R<row and C<col:
                    temp.append(mat[R][C])
                    R+=1
                    C+=1
                if flag:
                    temp.sort()
                    flag=False
                result[r][c] = temp[count]
                count+=1
                r+=1
                c+=1
                
        return result
​
​
