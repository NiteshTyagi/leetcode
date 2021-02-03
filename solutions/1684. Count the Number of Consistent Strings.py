class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count=0
        for word in words:
            breaked = 0
            for i in word:
                if i not in allowed:
                    breaked=1
                    break
            if breaked==0:
                count+=1
            
        return count
            
