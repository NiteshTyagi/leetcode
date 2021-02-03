class Solution:
    def interpret(self, command: str) -> str:
        return "o".join(command.split('()')).replace('(','').replace(')','')
        
