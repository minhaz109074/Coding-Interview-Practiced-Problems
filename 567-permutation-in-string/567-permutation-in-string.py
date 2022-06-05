class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1)
        beg, end = 0, len(s1)
        while(end<=len(s2)):
            window = s2[beg:end]
            if Counter(window) == s1_count:
                return True
            else:
                beg += 1
            end += 1
            
        return False
        