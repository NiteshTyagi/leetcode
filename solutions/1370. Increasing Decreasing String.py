class Solution:
    def sortString(self, s: str) -> str:
        s = list(s)
        result = ''
        def second_smallest(no_small):
            for i in sorted(s):
                if i>no_small:
                    temp = i
                    s.remove(i)
                    return temp
            return ''
        
        def second_largest(no_large):
            for i in sorted(s,reverse=True):
                if i<no_large:
                    temp = i
                    s.remove(i)
                    return temp
            return ''
        while s:    
            n = min(s)
            result += n
            no_small = n
            s.remove(n)
            while no_small:
                no_small = second_smallest(no_small)
                result+=no_small
            # print(result,s,sep='<---111--->')
            if s:
                t = max(s)
                no_large = t 
                result+=no_large
                s.remove(t)
​
                while no_large:
                    no_large = second_largest(no_large)
                    result+=no_large
                # print(result,s,sep='<---222--->')
        return result
        
