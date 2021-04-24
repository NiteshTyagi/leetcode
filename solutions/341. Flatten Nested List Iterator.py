# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """
​
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nestedList = nestedList
        self.stack = []
        self.flatten()
    
    def function(self,nl):
        if nl.isInteger():            
            return self.stack.append(nl.getInteger())
        else:
            for n in nl.getList():
                self.function(n)        
    
    def flatten(self):
        for nl in self.nestedList:
            self.function(nl)
    
    def next(self) -> int:
        top = self.stack.pop(0)
        return top
        
    
    def hasNext(self) -> bool:
        if self.stack:
            return True
        
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
