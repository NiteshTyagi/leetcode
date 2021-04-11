class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        size=len(edges)
        result=[]
        vertices = [i for i in range(size+1)]
        graph = {v:set([v]) for v in range(1,size+1)}
        
        def set_values(src,trgt):
            for uu in graph[vertices[src]]:
                graph[vertices[trgt]].add(uu)
                vertices[uu]=vertices[trgt]
                
        for u,v in edges:
            if graph[vertices[u]].isdisjoint(graph[vertices[v]]):
                if len(graph[vertices[u]])==1 and len(graph[vertices[v]])==1:
                    graph[vertices[u]].add(v)
                    for uu in graph[vertices[u]]:
                        vertices[uu]=u   
                elif len(graph[vertices[u]])>=len(graph[vertices[v]]):
                    set_values(v,u)
                elif len(graph[vertices[u]])<len(graph[vertices[v]]):
                    set_values(u,v)
            else:
                result.append([u,v])
​
        return result[-1]
