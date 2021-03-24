class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n=len(edges)
        vertices = {i:0 for i in range(1,n+2)}
        for a,b in edges:
            vertices[a]+=1
            vertices[b]+=1
            
        for k,v in vertices.items():
            if vertices[k]==n:
                return k
        # print(vertices)
