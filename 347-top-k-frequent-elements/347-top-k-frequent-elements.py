class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = Counter(nums)
        ans = []
        for x,y in m.most_common(k):
                ans.append(x)
               
        return ans
                
                     
                
        
            
        
        
        
        