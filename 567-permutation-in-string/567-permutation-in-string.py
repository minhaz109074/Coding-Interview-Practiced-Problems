class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #TC: O(n*26) 
        s1_count = Counter(s1)
        beg, end = 0, 0
        mp = defaultdict(int)
        count = 0
        while(end<len(s2)):
            mp[s2[end]] += 1
            if  count == len(s1)-1:
                if mp == s1_count:
                    return True
                else:
                    mp[s2[beg]] -= 1
                    count -= 1
                    if mp[s2[beg]] == 0:
                        del mp[s2[beg]]
                    beg += 1
            end += 1
            count += 1
            
        return False
        
