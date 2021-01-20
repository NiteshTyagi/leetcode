class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        Sstack = []
        Tstack = []
        for i in S:
            if Sstack and i=='#':
                Sstack.pop()
            elif i!='#':
                Sstack.append(i)
        for i in T:
            if Tstack and i=='#':
                Tstack.pop()
            elif i!='#':
                Tstack.append(i)
        return Sstack==Tstack
