class StockSpanner:
​
    def __init__(self):
        self.stack = []
        self.index = 0
​
        
    def next(self, price: int) -> int:
        if not self.stack:
            self.stack = [(0,price),]
            return 1
        self.index+=1
        if self.stack:
            while self.stack and self.stack[-1][1] <= price:
                self.stack.pop()
            if self.stack and self.stack[-1][1] > price:
                result = self.index-self.stack[-1][0]
                # return self.index-self.stack[-1][0]
            else:
                result = self.index+1
            self.stack.append((self.index,price))
        return result
​
        
​
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
