class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        final_result = []
        size = len(graph)
        for i in graph[0]:
            path = [0,i]
            adj_list = [[path.copy(),j] for j in graph[i]]
            if not adj_list:
                final_result.append(path)
            while adj_list:
                path,node = adj_list.pop()
                if not graph[node]:
                    if node==size-1:
                        path.append(node)
                        final_result.append(path)
                    elif path[-1]==size-1:
                        final_result.append(path)
​
                else:
                    path.append(node)
                    adj_list.extend([[path.copy(),j] for j in graph[node]])
                    
        return final_result
            
        
