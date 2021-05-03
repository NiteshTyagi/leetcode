class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i:[] for i in range(numCourses) }
        
        for source,dest in prerequisites:
            graph[dest].append(source)
        
        in_degree =  [0 for vertice in graph.keys()]
        for vertice in graph:
            for v in graph[vertice]:
                in_degree[v]+=1
                
        queue = list()
        
        for v in graph:
            if in_degree[v]==0:
                queue.append(v)
                
        result = list()
        
        while queue:
            ele = queue.pop(0)
            result.append(ele)
​
            for v in graph[ele]:
                in_degree[v]-=1
                if in_degree[v]==0:
                    queue.append(v)
        
        return [] if len(result)!=len(graph) else result 
