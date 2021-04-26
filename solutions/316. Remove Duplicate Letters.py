class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        visited = []
        counter = dict()
        size = len(s)
        for index in range(size):
            counter[s[index]]=index
        
        for index in range(size):
            currentele  = s[index]
            if not stack:
                stack.append(currentele)
                visited.append(currentele)
            else:
                if currentele not in stack:
                    if currentele>stack[-1] and currentele not in visited:
                        stack.append(currentele)
                        visited.append(currentele)
                    else:
                        top = stack[-1]
                        while stack and currentele<top and top in counter:
                            stack.pop()
                            visited.pop()
                            if stack:
                                top = stack[-1]
                            else:
                                break
                        stack.append(currentele)
                        visited.append(currentele)
            if counter[currentele]==index:
                del counter[currentele]
        return "".join(stack)
