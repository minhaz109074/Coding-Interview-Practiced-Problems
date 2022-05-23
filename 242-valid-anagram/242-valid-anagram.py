class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        scount = Counter(s)
        tcount = Counter(t)
        
        if scount == tcount:
            return True
        else:
            return False