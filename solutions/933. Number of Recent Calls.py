class RecentCounter:
​
    def __init__(self):
        self.request = []
        
​
    def ping(self, t: int) -> int:
        self.request.append(t)
        range_var = [t-3000,t]
        
        for i in range(len(self.request)-1,-1,-1):
            if not range_var[0]<=self.request[i]<=range_var[1]:
                self.request = self.request[i+1:]
                return len(self.request)
        return len(self.request)
            
        
# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
