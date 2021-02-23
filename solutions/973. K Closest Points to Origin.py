class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []
        def euclidean(point):
            return (point[0]-0)**2+(point[1]-0)**2
        
        for point in points:
            distance = euclidean(point)
            result.append((distance,point))
        result.sort(key=lambda x:x[0])
        r = [result[i][1] for i in range(k)]
        return r
