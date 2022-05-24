class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = Counter(nums)
        count = 1
        ans = []
        for x,y in sorted(m.items(), key = lambda num: num[1], reverse = True):
                if count <= k:
                    ans.append(x)
                else:
                    break
                count += 1
        return ans
                
                     
                
        
            
        
        
        
        