class MyCircularQueue:
​
    def __init__(self, k: int):
        self.size = k
        self.queue = [None]*k
        self.front = self.rear = -1
        
​
    def enQueue(self, value: int) -> bool:
        if((self.rear+1)%self.size==self.front):
            return False
        elif self.front==-1 and self.rear==-1:
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = value
            
        else:
            self.rear = (self.rear+1)%self.size
            self.queue[self.rear] = value
        return True
​
    def deQueue(self) -> bool:
        if self.front==-1:
            return False
        elif self.front==self.rear:
            self.queue[self.front]=None
            self.front=-1
            self.rear=-1
        else:
            self.queue[self.front]=None
            self.front = (self.front+1)%self.size
        return True
            
    def Front(self) -> int:
        return self.queue[self.front] if self.queue[self.front]!=None  else -1
        
    def Rear(self) -> int:
        # print(self.queue,self.rear)
        return self.queue[self.rear] if self.queue[self.rear]!=None else -1
        
    def isEmpty(self) -> bool:
        return all(v is None for v in self.queue)
​
    def isFull(self) -> bool:
        return all(self.queue)
