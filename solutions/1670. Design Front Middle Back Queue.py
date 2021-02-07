class FrontMiddleBackQueue:
​
    def __init__(self):
        self.queue = []
        
    def pushFront(self, val: int) -> None:
        self.queue.insert(0,val)
        return None
​
    def pushMiddle(self, val: int) -> None:
        if self.queue:
            middle_index = len(self.queue)//2
            self.queue.insert(middle_index,val)
        else:
            self.queue.insert(0,val)
        return None
​
    def pushBack(self, val: int) -> None:
        self.queue.append(val)
        return None
​
    def popFront(self) -> int:
