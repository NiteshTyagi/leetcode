class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        from collections import Counter
        countt = Counter(t)
        counts = Counter(s)
        diff = countt-counts
        return (max(diff.keys(),key=diff.get))
