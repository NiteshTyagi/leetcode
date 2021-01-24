class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = [(0,T[0]),]
        index = [0]*len(T)
        for i in range(1,len(T)):
            # next_element = T[i]
            if stack:
                element = stack.pop()
                while element[1]<T[i]:
                    index[element[0]]=i-element[0]
                    if not stack:
                        break
                    element = stack.pop()
                if element[1]>=T[i]:
                    stack.append(element)
            stack.append((i,T[i]))
        while stack:
            element = stack.pop()
            index[element[0]]=0
        return index
    
                
            
        
