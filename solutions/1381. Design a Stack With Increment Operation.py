class CustomStack:
​
    def __init__(self, maxSize: int):
        self.stack = []
        self.maxSize = maxSize
        
​
    def push(self, x: int) -> None:
        if len(self.stack)<self.maxSize:
            return self.stack.append(x)
    
    def pop(self) -> int:
        return self.stack.pop() if self.stack else -1
        
​
    def increment(self, k: int, val: int) -> None:
        self.stack[:k] = [val+i for i in self.stack[:k]] 
        return self.stack
​
# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
