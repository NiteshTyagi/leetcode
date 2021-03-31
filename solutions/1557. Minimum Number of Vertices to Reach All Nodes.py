class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        vertices = [False]*n
        for edge in edges:
            vertices[edge[1]]=True
        edges = []
        for i in range(n):
            if not vertices[i]:
                edges.append(i)
        return edges
