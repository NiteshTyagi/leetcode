class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i:[] for i in range(numCourses) }
        
        for source,dest in prerequisites:
            graph[source].append(dest)
        
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
        
        return False if len(result)!=len(graph) else True 
                    
            
                    
