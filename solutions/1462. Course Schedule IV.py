class Solution:
    def __init__(self):
        self.graph = dict()
        self.result = []
        
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        if not prerequisites:
            return [False]*len(queries)
        
        self.graph = {i:[] for i in range(numCourses)}
        
        for src,dest in prerequisites:
            self.graph[src].append(dest)
            
        queue = list()
        result = []
        
        for query in queries:
            visited = [False]*numCourses
            if query in prerequisites:
                result.append(True)
            else:
                c=0
                dest = query[1]
                src = query[0]
                visited[src]=True
                queue.append(src)
                while queue:
                    ele = queue.pop(0)
                    for adj in self.graph[ele]:
                        if visited[adj]==False:
                            if adj==dest:
                                c=0
                                result.append(True)
                                queue=[]
                                break
                            else:
