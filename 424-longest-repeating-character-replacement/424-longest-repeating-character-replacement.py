class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #TC: O(n*26), SC: O(26)
        beg, end, ans = 0,0,0
        mp = defaultdict(int)
        n = len(s)
        while(end<n):
            mp[s[end]] += 1
            while (end-beg+1) - max(mp.values()) > k:
                mp[s[beg]] -= 1
                beg += 1
            ans = max(ans, end-beg+1)
            end += 1
        return ans
                
                        
                    
                
        