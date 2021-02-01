from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = list(collections.Counter(tasks).values())
        print(task_counts)
        M = max(task_counts)
        Mct = task_counts.count(M)
        return max(len(tasks), (M - 1) * (n + 1) + Mct)
            
            
        
